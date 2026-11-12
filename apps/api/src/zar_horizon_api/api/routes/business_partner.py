import json
import logging
from datetime import UTC, datetime
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from zar_horizon_api.api.dependencies import (
    BusinessPartnerContext,
    get_business_partner_context,
    get_db,
)
from zar_horizon_api.core.config import Settings, get_settings
from zar_horizon_api.models.business_partner import (
    BusinessAction,
    BusinessAnalysis,
    BusinessProfile,
    FinancialImport,
    FinancialTransaction,
)
from zar_horizon_api.models.platform import AuditEvent
from zar_horizon_api.schemas.business_partner import (
    AnalysisRequest,
    AnalysisResponse,
    BusinessActionCreate,
    BusinessActionResponse,
    BusinessActionStatusUpdate,
    BusinessProfileResponse,
    BusinessProfileUpsert,
    CsvImportResponse,
    CsvPreviewRequest,
    CsvPreviewResponse,
    EvidenceResponse,
    FinancialSummaryResponse,
    InsightResponse,
    TransactionPreviewRow,
)
from zar_horizon_api.services.business_partner import (
    CSVFormatError,
    ParsedTransaction,
    build_evidence_and_insights,
    mark_existing_duplicates,
    parse_financial_csv,
    summarize_transactions,
)
from zar_horizon_api.services.insight_provider import (
    ProviderConfigurationError,
    ProviderResponseError,
    ProviderUnavailable,
    create_insight_provider,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/business", tags=["business-partner"])


def _profile_query(context: BusinessPartnerContext):
    return select(BusinessProfile).where(
        BusinessProfile.organization_id == context.organization_id,
        BusinessProfile.workspace_id == context.workspace_id,
    )


def _require_profile(db: Session, context: BusinessPartnerContext) -> BusinessProfile:
    profile = db.scalar(_profile_query(context))
    if profile is None:
        raise HTTPException(
            status_code=409,
            detail="Create a business profile before importing or analysing financial records.",
        )
    return profile


def _record_audit_event(
    db: Session, context: BusinessPartnerContext, action: str
) -> None:
    db.add(
        AuditEvent(
            organization_id=context.organization_id,
            workspace_id=context.workspace_id,
            actor_user_id=None,
            action=action,
        )
    )


def _transaction_query(context: BusinessPartnerContext):
    return select(FinancialTransaction).where(
        FinancialTransaction.organization_id == context.organization_id,
        FinancialTransaction.workspace_id == context.workspace_id,
    )


def _preview_rows(rows: list[ParsedTransaction]) -> list[TransactionPreviewRow]:
    return [
        TransactionPreviewRow(
            line_number=row.line_number,
            status=row.status,
            errors=list(row.errors),
            transaction_date=row.transaction_date,
            description=row.description,
            transaction_type=row.transaction_type,
            category=row.category,
            amount=row.amount,
            currency=row.currency,
        )
        for row in rows
    ]


def _prepare_preview(
    db: Session,
    context: BusinessPartnerContext,
    request: CsvPreviewRequest,
) -> tuple[CsvPreviewResponse, list[ParsedTransaction], str]:
    _require_profile(db, context)
    try:
        content_hash, rows = parse_financial_csv(request.csv_text, request.decimal_format)
    except CSVFormatError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    existing_import = db.scalar(
        select(FinancialImport).where(
            FinancialImport.organization_id == context.organization_id,
            FinancialImport.workspace_id == context.workspace_id,
            FinancialImport.content_hash == content_hash,
        )
    )
    fingerprints = {row.fingerprint for row in rows if row.fingerprint}
    existing_fingerprints: set[str] = set()
    if fingerprints:
        existing_fingerprints = set(
            db.scalars(
                select(FinancialTransaction.fingerprint).where(
                    FinancialTransaction.organization_id == context.organization_id,
                    FinancialTransaction.workspace_id == context.workspace_id,
                    FinancialTransaction.fingerprint.in_(fingerprints),
                )
            ).all()
        )

    rows = mark_existing_duplicates(rows, existing_fingerprints)
    if existing_import is not None:
        rows = [
            ParsedTransaction(
                line_number=row.line_number,
                status="duplicate" if row.status == "valid" else row.status,
                errors=(
                    ("This exact file was imported previously; no rows will be imported.",)
                    if row.status == "valid"
                    else row.errors
                ),
                transaction_date=row.transaction_date,
                description=row.description,
                transaction_type=row.transaction_type,
                category=row.category,
                amount=row.amount,
                currency=row.currency,
                source_reference=row.source_reference,
                fingerprint=row.fingerprint,
            )
            for row in rows
        ]

    preview = CsvPreviewResponse(
        file_duplicate=existing_import is not None,
        rows=_preview_rows(rows),
        valid_count=sum(row.status == "valid" for row in rows),
        invalid_count=sum(row.status == "invalid" for row in rows),
        duplicate_count=sum(row.status == "duplicate" for row in rows),
    )
    return preview, rows, content_hash


def _financial_summary(db: Session, context: BusinessPartnerContext) -> FinancialSummaryResponse:
    transactions = db.scalars(
        _transaction_query(context).order_by(FinancialTransaction.transaction_date)
    ).all()
    summary = summarize_transactions(transactions)
    latest_import = db.scalar(
        select(FinancialImport)
        .where(
            FinancialImport.organization_id == context.organization_id,
            FinancialImport.workspace_id == context.workspace_id,
        )
        .order_by(FinancialImport.created_at.desc())
        .limit(1)
    )
    return FinancialSummaryResponse(
        transaction_count=int(summary["transaction_count"]),
        currencies=summary["currencies"],
        latest_import_at=latest_import.created_at if latest_import else None,
    )


@router.get("/profile", response_model=BusinessProfileResponse)
def get_business_profile(
    context: BusinessPartnerContext = Depends(get_business_partner_context),
    db: Session = Depends(get_db),
) -> BusinessProfile:
    profile = db.scalar(_profile_query(context))
    if profile is None:
        raise HTTPException(status_code=404, detail="No business profile has been created yet.")
    return profile


@router.post(
    "/profile",
    response_model=BusinessProfileResponse,
    status_code=status.HTTP_200_OK,
)
def save_business_profile(
    payload: BusinessProfileUpsert,
    context: BusinessPartnerContext = Depends(get_business_partner_context),
    db: Session = Depends(get_db),
) -> BusinessProfile:
    profile = db.scalar(_profile_query(context))
    if profile is None:
        profile = BusinessProfile(
            id=uuid4(),
            organization_id=context.organization_id,
            workspace_id=context.workspace_id,
            **payload.model_dump(),
        )
        db.add(profile)
        audit_action = "business_profile.created"
    else:
        for field, value in payload.model_dump().items():
            setattr(profile, field, value)
        audit_action = "business_profile.updated"
    _record_audit_event(db, context, audit_action)
    db.commit()
    db.refresh(profile)
    return profile


@router.post("/financial/import/preview", response_model=CsvPreviewResponse)
def preview_financial_import(
    payload: CsvPreviewRequest,
    context: BusinessPartnerContext = Depends(get_business_partner_context),
    db: Session = Depends(get_db),
) -> CsvPreviewResponse:
    preview, _, _ = _prepare_preview(db, context, payload)
    return preview


@router.post("/financial/import", response_model=CsvImportResponse)
def import_financial_csv(
    payload: CsvPreviewRequest,
    context: BusinessPartnerContext = Depends(get_business_partner_context),
    db: Session = Depends(get_db),
) -> CsvImportResponse:
    preview, rows, content_hash = _prepare_preview(db, context, payload)
    if preview.file_duplicate:
        raise HTTPException(status_code=409, detail="This exact CSV file has already been imported.")

    valid_rows = [row for row in rows if row.status == "valid"]
    if not valid_rows:
        raise HTTPException(
            status_code=422,
            detail="No valid, unique rows are available to import. Review the preview first.",
        )
    profile = _require_profile(db, context)
    import_record = FinancialImport(
        id=uuid4(),
        organization_id=context.organization_id,
        workspace_id=context.workspace_id,
        content_hash=content_hash,
        file_name=payload.file_name,
        decimal_format=payload.decimal_format,
        row_count=len(rows),
        imported_count=len(valid_rows),
    )
    db.add(import_record)
    db.flush()
    for row in valid_rows:
        if (
            row.transaction_date is None
            or row.description is None
            or row.transaction_type is None
            or row.category is None
            or row.amount is None
            or row.currency is None
            or row.fingerprint is None
        ):
            raise HTTPException(
                status_code=500,
                detail="A validated import row was missing required normalized data.",
            )
        db.add(
            FinancialTransaction(
                organization_id=context.organization_id,
                workspace_id=context.workspace_id,
                business_profile_id=profile.id,
                import_id=import_record.id,
                transaction_date=row.transaction_date,
                description=row.description,
                transaction_type=row.transaction_type,
                category=row.category,
                amount=row.amount,
                currency=row.currency,
                source_reference=row.source_reference,
                fingerprint=row.fingerprint,
                source_line=row.line_number,
            )
        )

    _record_audit_event(db, context, "business_financial_import.created")
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A matching import was saved concurrently. Refresh the preview before retrying.",
        ) from exc
    db.refresh(import_record)
    return CsvImportResponse(
        import_id=import_record.id,
        file_duplicate=False,
        rows=preview.rows,
        valid_count=preview.valid_count,
        invalid_count=preview.invalid_count,
        duplicate_count=preview.duplicate_count,
        imported_count=len(valid_rows),
    )


@router.get("/financial/summary", response_model=FinancialSummaryResponse)
def get_financial_summary(
    context: BusinessPartnerContext = Depends(get_business_partner_context),
    db: Session = Depends(get_db),
) -> FinancialSummaryResponse:
    _require_profile(db, context)
    return _financial_summary(db, context)


@router.post("/analysis", response_model=AnalysisResponse)
def analyse_business_performance(
    payload: AnalysisRequest,
    context: BusinessPartnerContext = Depends(get_business_partner_context),
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> AnalysisResponse:
    profile = _require_profile(db, context)
    financial_summary = _financial_summary(db, context)
    summary_data = json.loads(financial_summary.model_dump_json())
    evidence, deterministic_insights = build_evidence_and_insights(summary_data)
    ai_insights: list[dict[str, object]] = []
    answer: str | None = None
    answer_evidence_ids: list[str] = []
    summary_evidence_ids: list[str] = []
    if financial_summary.transaction_count == 0:
        ai_status = "not_available"
        ai_message = "No validated financial records are available. Import records before analysis."
        summary_text = "There are no validated financial transactions to analyse."
    else:
        try:
            provider = create_insight_provider(settings)
        except ProviderConfigurationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc

        if provider is None:
            ai_status = "not_configured"
            ai_message = (
                "AI provider is not configured. Deterministic calculations and findings are "
                "available; natural-language question answering is unavailable."
            )
            summary_text = (
                "Financial results were calculated from validated imported records. "
                "Review the cited figures, periods, and assumptions below."
            )
            summary_evidence_ids = [str(item["id"]) for item in evidence]
        else:
            try:
                generated = provider.analyse(
                    question=payload.question,
                    summary=summary_data,
                    deterministic_insights=deterministic_insights,
                    evidence_ids={str(item["id"]) for item in evidence},
                )
            except ProviderUnavailable as exc:
                logger.warning("AI insight provider unavailable")
                raise HTTPException(
                    status_code=502,
                    detail="AI provider is unavailable. Financial summaries remain available.",
                ) from exc
            except ProviderResponseError as exc:
                logger.warning("AI insight provider returned an invalid response")
                raise HTTPException(
                    status_code=502,
                    detail="AI provider returned an unusable response. No AI insight was saved.",
                ) from exc
            ai_status = "available"
            ai_message = "AI analysis is grounded in the validated summary and cited evidence shown."
            summary_text = generated.summary
            summary_evidence_ids = generated.summary_evidence_ids
            answer = generated.answer
            answer_evidence_ids = generated.answer_evidence_ids
            ai_insights = [
                insight.model_dump(mode="json") | {"id": f"ai_{index}", "origin": "ai"}
                for index, insight in enumerate(generated.insights, start=1)
            ]

    analysis_data: dict[str, object] = {
        "summary": summary_text,
        "summary_evidence_ids": summary_evidence_ids,
        "answer": answer,
        "answer_evidence_ids": answer_evidence_ids,
        "deterministic_insights": deterministic_insights,
        "ai_insights": ai_insights,
    }
    evidence_json = [
        EvidenceResponse.model_validate(item).model_dump(mode="json") for item in evidence
    ]
    analysis = BusinessAnalysis(
        id=uuid4(),
        organization_id=context.organization_id,
        workspace_id=context.workspace_id,
        business_profile_id=profile.id,
        question=payload.question,
        ai_status=ai_status,
        analysis_data=analysis_data,
        evidence_data=evidence_json,
    )
    db.add(analysis)
    _record_audit_event(db, context, "business_analysis.created")
    db.commit()
    return AnalysisResponse(
        analysis_id=analysis.id,
        ai_status=ai_status,
        ai_message=ai_message,
        summary=summary_text,
        summary_evidence_ids=summary_evidence_ids,
        answer=answer,
        answer_evidence_ids=answer_evidence_ids,
        deterministic_insights=[
            InsightResponse.model_validate(item) for item in deterministic_insights
        ],
        ai_insights=[InsightResponse.model_validate(item) for item in ai_insights],
        evidence=[EvidenceResponse.model_validate(item) for item in evidence_json],
    )


@router.get("/actions", response_model=list[BusinessActionResponse])
def list_business_actions(
    context: BusinessPartnerContext = Depends(get_business_partner_context),
    db: Session = Depends(get_db),
) -> list[BusinessAction]:
    return list(
        db.scalars(
            select(BusinessAction)
            .where(
                BusinessAction.organization_id == context.organization_id,
                BusinessAction.workspace_id == context.workspace_id,
            )
            .order_by(BusinessAction.created_at.desc())
        ).all()
    )


@router.post(
    "/actions",
    response_model=BusinessActionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_business_action(
    payload: BusinessActionCreate,
    context: BusinessPartnerContext = Depends(get_business_partner_context),
    db: Session = Depends(get_db),
) -> BusinessAction:
    analysis = db.scalar(
        select(BusinessAnalysis).where(
            BusinessAnalysis.id == payload.analysis_id,
            BusinessAnalysis.organization_id == context.organization_id,
            BusinessAnalysis.workspace_id == context.workspace_id,
        )
    )
    if analysis is None:
        raise HTTPException(status_code=404, detail="Analysis was not found in this workspace.")

    analysis_insights = analysis.analysis_data
    all_insights = analysis_insights.get("deterministic_insights", []) + analysis_insights.get(
        "ai_insights", []
    )
    insight = next(
        (
            item
            for item in all_insights
            if isinstance(item, dict) and item.get("id") == payload.insight_id
        ),
        None,
    )
    if insight is None:
        raise HTTPException(status_code=404, detail="Insight was not found in this analysis.")

    evidence_by_id = {item["id"]: item for item in analysis.evidence_data}
    evidence_ids = insight.get("evidence_ids", [])
    supporting_evidence = [
        evidence_by_id[evidence_id]
        for evidence_id in evidence_ids
        if evidence_id in evidence_by_id
    ]
    if not supporting_evidence:
        raise HTTPException(
            status_code=422,
            detail="An action requires supporting evidence from the selected insight.",
        )
    recommendation = str(insight["recommended_action"])
    action = BusinessAction(
        id=uuid4(),
        organization_id=context.organization_id,
        workspace_id=context.workspace_id,
        analysis_id=analysis.id,
        source_insight_id=payload.insight_id,
        title=(payload.title or recommendation).strip(),
        description=(payload.description or recommendation).strip(),
        reason=str(insight["description"]),
        priority=str(insight["priority"]),
        status="open",
        external_execution_status="not_executed",
        supporting_evidence=supporting_evidence,
    )
    db.add(action)
    _record_audit_event(db, context, "business_action.created")
    db.commit()
    db.refresh(action)
    return action


@router.patch("/actions/{action_id}", response_model=BusinessActionResponse)
def update_business_action(
    action_id: UUID,
    payload: BusinessActionStatusUpdate,
    context: BusinessPartnerContext = Depends(get_business_partner_context),
    db: Session = Depends(get_db),
) -> BusinessAction:
    action = db.scalar(
        select(BusinessAction).where(
            BusinessAction.id == action_id,
            BusinessAction.organization_id == context.organization_id,
            BusinessAction.workspace_id == context.workspace_id,
        )
    )
    if action is None:
        raise HTTPException(status_code=404, detail="Action was not found in this workspace.")

    allowed_transitions = {
        "open": {"open", "in_progress", "completed", "cancelled"},
        "in_progress": {"open", "in_progress", "completed", "cancelled"},
        "completed": {"completed"},
        "cancelled": {"cancelled"},
    }
    if payload.status not in allowed_transitions[action.status]:
        raise HTTPException(
            status_code=409,
            detail=f"Action cannot transition from {action.status} to {payload.status}.",
        )
    if payload.status == "completed" and not payload.outcome:
        raise HTTPException(
            status_code=422,
            detail="Record the outcome before marking an internal action completed.",
        )

    action.status = payload.status
    action.outcome = payload.outcome
    if payload.status == "completed":
        action.completed_at = action.completed_at or datetime.now(UTC)
    else:
        action.completed_at = None
    _record_audit_event(db, context, "business_action.updated")
    db.commit()
    db.refresh(action)
    return action
