import json
from decimal import Decimal

import httpx
import pytest
from fastapi.testclient import TestClient
from pydantic import SecretStr
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from zar_horizon_api import models
from zar_horizon_api.api.dependencies import get_db
from zar_horizon_api.core.config import Settings, get_settings
from zar_horizon_api.database.base import Base
from zar_horizon_api.main import app
from zar_horizon_api.services.business_partner import (
    CSVFormatError,
    parse_financial_csv,
    summarize_transactions,
)
from zar_horizon_api.services.insight_provider import (
    OpenAICompatibleInsightProvider,
    ProviderResponseError,
)

_ = models

CSV_FIXTURE = """date,description,amount,currency,type,category
2025-01-03,Shop sales,10000.00,ZAR,revenue,Sales
05/01/2025,Shop rent,3000.00,ZAR,expense,Rent
2025-02-03,Shop sales,8000.00,RAND,income,Sales
2025-02-05,Shop rent,3500.00,ZAR,expense,Rent
2025-02-05,Shop rent,3500.00,ZAR,expense,Rent
not-a-date,Unclassified row,50.00,ZAR,,Other
"""


@pytest.fixture
def client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    @event.listens_for(engine, "connect")
    def enable_foreign_keys(connection, _record):
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    Base.metadata.create_all(engine)
    test_session = sessionmaker(bind=engine, autoflush=False)

    def override_db():
        session = test_session()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_db
    app.dependency_overrides[get_settings] = lambda: Settings(
        app_env="test",
        business_partner_local_mode=True,
        database_url="sqlite://",
    )
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(engine)
    engine.dispose()


def create_profile(client: TestClient) -> None:
    response = client.post(
        "/api/v1/business/profile",
        json={"business_name": "Cape Town Corner Store", "industry": "Retail"},
    )
    assert response.status_code == 200


def test_financial_calculation_uses_explicit_types_and_separates_currency() -> None:
    content = """date,description,amount,currency,type,category
2025-01-01,Sales,1250.50,ZAR,revenue,Sales
2025-01-02,Stock,300.25,ZAR,expense,Inventory
2025-01-03,Export sale,100.00,USD,revenue,Sales
"""
    _, rows = parse_financial_csv(content, "dot")
    summary = summarize_transactions(
        [
            type(
                "Transaction",
                (),
                {
                    "transaction_date": row.transaction_date,
                    "description": row.description,
                    "transaction_type": row.transaction_type,
                    "category": row.category,
                    "amount": row.amount,
                    "currency": row.currency,
                },
            )()
            for row in rows
        ]
    )

    zar = next(item for item in summary["currencies"] if item["currency"] == "ZAR")
    usd = next(item for item in summary["currencies"] if item["currency"] == "USD")
    assert zar["revenue"] == Decimal("1250.50")
    assert zar["expenses"] == Decimal("300.25")
    assert zar["net_profit"] == Decimal("950.25")
    assert zar["expense_categories"][0]["share_percent"] == Decimal("100.00")
    assert usd["revenue"] == Decimal("100.00")
    assert usd["expenses"] == Decimal("0.00")


def test_csv_rejects_missing_classification_and_ambiguous_amount() -> None:
    content = """date,description,amount,currency,type
2025-01-01,Unknown type,10.00,ZAR,
2025-01-02,Ambiguous amount,1,234,ZAR,revenue
"""
    _, rows = parse_financial_csv(content, "dot")
    assert rows[0].status == "invalid"
    assert any("not inferred" in error for error in rows[0].errors)
    assert rows[1].status == "invalid"
    with pytest.raises(CSVFormatError, match="missing required columns"):
        parse_financial_csv("date,amount\n2025-01-01,3", "dot")


def test_import_preview_summary_analysis_and_action_tracking(client: TestClient) -> None:
    create_profile(client)
    preview = client.post(
        "/api/v1/business/financial/import/preview",
        json={"file_name": "synthetic.csv", "csv_text": CSV_FIXTURE, "decimal_format": "dot"},
    )
    assert preview.status_code == 200
    assert preview.json()["valid_count"] == 4
    assert preview.json()["invalid_count"] == 1
    assert preview.json()["duplicate_count"] == 1
    assert preview.json()["rows"][2]["transaction_date"] == "2025-02-03"

    imported = client.post(
        "/api/v1/business/financial/import",
        json={"file_name": "synthetic.csv", "csv_text": CSV_FIXTURE, "decimal_format": "dot"},
    )
    assert imported.status_code == 200
    assert imported.json()["imported_count"] == 4

    summary = client.get("/api/v1/business/financial/summary")
    assert summary.status_code == 200
    financials = summary.json()["currencies"][0]
    assert financials["revenue"] == "18000.00"
    assert financials["expenses"] == "6500.00"
    assert financials["net_profit"] == "11500.00"
    assert [period["period"] for period in financials["periods"]] == ["2025-01", "2025-02"]

    duplicate = client.post(
        "/api/v1/business/financial/import",
        json={"file_name": "synthetic.csv", "csv_text": CSV_FIXTURE, "decimal_format": "dot"},
    )
    assert duplicate.status_code == 409

    analysis = client.post(
        "/api/v1/business/analysis",
        json={"question": "What changed in the imported records?"},
    )
    assert analysis.status_code == 200
    analysis_body = analysis.json()
    assert analysis_body["ai_status"] == "not_configured"
    assert analysis_body["answer"] is None
    evidence_ids = {item["id"] for item in analysis_body["evidence"]}
    assert set(analysis_body["summary_evidence_ids"]).issubset(evidence_ids)
    assert analysis_body["deterministic_insights"]

    insight = analysis_body["deterministic_insights"][0]
    action = client.post(
        "/api/v1/business/actions",
        json={
            "analysis_id": analysis_body["analysis_id"],
            "insight_id": insight["id"],
        },
    )
    assert action.status_code == 201
    action_body = action.json()
    assert action_body["external_execution_status"] == "not_executed"
    assert action_body["supporting_evidence"]

    incomplete = client.patch(
        f"/api/v1/business/actions/{action_body['id']}",
        json={"status": "completed"},
    )
    assert incomplete.status_code == 422
    completed = client.patch(
        f"/api/v1/business/actions/{action_body['id']}",
        json={"status": "completed", "outcome": "Reviewed source records with the bookkeeper"},
    )
    assert completed.status_code == 200
    assert completed.json()["status"] == "completed"
    assert completed.json()["external_execution_status"] == "not_executed"


def test_local_workspace_routes_are_disabled_without_explicit_development_flag(
    client: TestClient,
) -> None:
    app.dependency_overrides[get_settings] = lambda: Settings(
        app_env="production",
        business_partner_local_mode=True,
        database_url="sqlite://",
    )
    response = client.get("/api/v1/business/profile")
    assert response.status_code == 404


def test_ai_provider_requires_citations_to_known_evidence() -> None:
    generated_content = {
        "summary": "Revenue increased while expenses also rose.",
        "summary_evidence_ids": ["revenue:ZAR"],
        "answer": "The dataset shows changes across the reporting periods.",
        "answer_evidence_ids": ["revenue:ZAR"],
        "insights": [],
    }

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["authorization"] == "Bearer test-key"
        return httpx.Response(
            200,
            json={
                "choices": [
                    {"message": {"content": json.dumps(generated_content)}}
                ]
            },
        )

    provider = OpenAICompatibleInsightProvider(
        api_key=SecretStr("test-key"),
        chat_completions_url="https://provider.test/v1/chat/completions",
        model="test-model",
        transport=httpx.MockTransport(handler),
    )
    result = provider.analyse(
        question="What changed?",
        summary={"transaction_count": 1},
        deterministic_insights=[],
        evidence_ids={"revenue:ZAR"},
    )
    assert result.answer_evidence_ids == ["revenue:ZAR"]

    generated_content["answer_evidence_ids"] = ["unsupported"]
    with pytest.raises(ProviderResponseError, match="evidence"):
        provider.analyse(
            question="What changed?",
            summary={"transaction_count": 1},
            deterministic_insights=[],
            evidence_ids={"revenue:ZAR"},
        )
