from datetime import date, datetime
from decimal import Decimal
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


class BusinessProfileUpsert(BaseModel):
    business_name: str = Field(min_length=1, max_length=200)
    business_type: str | None = Field(default=None, max_length=120)
    industry: str | None = Field(default=None, max_length=120)
    country: str = Field(default="ZA", min_length=2, max_length=2)
    currency_code: str = Field(default="ZAR", min_length=3, max_length=3)
    region: str | None = Field(default=None, max_length=120)

    @field_validator("business_name", "business_type", "industry", "region")
    @classmethod
    def strip_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned or None

    @field_validator("country", "currency_code")
    @classmethod
    def uppercase_codes(cls, value: str) -> str:
        return value.strip().upper()


class BusinessProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    business_name: str
    business_type: str | None
    industry: str | None
    country: str
    currency_code: str
    region: str | None
    created_at: datetime
    updated_at: datetime


class CsvPreviewRequest(BaseModel):
    file_name: str = Field(min_length=1, max_length=255)
    csv_text: str = Field(min_length=1, max_length=2_000_000)
    decimal_format: Literal["dot", "comma"] = "dot"


class TransactionPreviewRow(BaseModel):
    line_number: int
    status: Literal["valid", "invalid", "duplicate"]
    errors: list[str]
    transaction_date: date | None
    description: str | None
    transaction_type: Literal["revenue", "expense"] | None
    category: str | None
    amount: Decimal | None
    currency: str | None


class CsvPreviewResponse(BaseModel):
    file_duplicate: bool
    rows: list[TransactionPreviewRow]
    valid_count: int
    invalid_count: int
    duplicate_count: int
    imported_count: int | None = None


class CsvImportResponse(CsvPreviewResponse):
    import_id: UUID


class FinancialCategorySummary(BaseModel):
    category: str
    amount: Decimal
    share_percent: Decimal | None


class FinancialPeriodSummary(BaseModel):
    period: str
    revenue: Decimal
    expenses: Decimal
    net_profit: Decimal
    profit_margin_percent: Decimal | None


class CurrencyFinancialSummary(BaseModel):
    currency: str
    revenue: Decimal
    expenses: Decimal
    net_profit: Decimal
    profit_margin_percent: Decimal | None
    periods: list[FinancialPeriodSummary]
    expense_categories: list[FinancialCategorySummary]


class FinancialSummaryResponse(BaseModel):
    transaction_count: int
    currencies: list[CurrencyFinancialSummary]
    latest_import_at: datetime | None


class AnalysisRequest(BaseModel):
    question: str | None = Field(default=None, max_length=1000)

    @field_validator("question")
    @classmethod
    def normalize_question(cls, value: str | None) -> str | None:
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned or None


class InsightResponse(BaseModel):
    id: str
    title: str
    description: str
    recommended_action: str
    priority: Literal["low", "medium", "high"]
    evidence_ids: list[str]
    origin: Literal["deterministic", "ai"]


class EvidenceResponse(BaseModel):
    id: str
    label: str
    value: str
    currency: str | None = None
    period: str | None = None


class AnalysisResponse(BaseModel):
    analysis_id: UUID
    ai_status: Literal["not_configured", "not_available", "available"]
    ai_message: str
    summary: str
    summary_evidence_ids: list[str]
    answer: str | None
    answer_evidence_ids: list[str]
    deterministic_insights: list[InsightResponse]
    ai_insights: list[InsightResponse]
    evidence: list[EvidenceResponse]


class BusinessActionCreate(BaseModel):
    analysis_id: UUID
    insight_id: str = Field(min_length=1, max_length=120)
    title: str | None = Field(default=None, max_length=200)
    description: str | None = Field(default=None, max_length=2000)


class BusinessActionStatusUpdate(BaseModel):
    status: Literal["open", "in_progress", "completed", "cancelled"]
    outcome: str | None = Field(default=None, max_length=2000)

    @field_validator("outcome")
    @classmethod
    def normalize_outcome(cls, value: str | None) -> str | None:
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned or None


class BusinessActionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    analysis_id: UUID
    source_insight_id: str
    title: str
    description: str
    reason: str
    priority: str
    status: str
    outcome: str | None
    external_execution_status: str
    supporting_evidence: list[EvidenceResponse]
    created_at: datetime
    completed_at: datetime | None
