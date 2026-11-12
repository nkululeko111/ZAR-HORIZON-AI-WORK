from datetime import date, datetime
from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy import (
    JSON,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKeyConstraint,
    Integer,
    Numeric,
    String,
    UniqueConstraint,
    Uuid,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from zar_horizon_api.database.base import Base


class BusinessProfile(Base):
    __tablename__ = "business_profiles"
    __table_args__ = (
        UniqueConstraint("organization_id", "workspace_id", name="uq_business_profiles_workspace"),
        UniqueConstraint(
            "organization_id",
            "workspace_id",
            "id",
            name="uq_business_profiles_org_workspace_id",
        ),
        ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    organization_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    workspace_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    business_name: Mapped[str] = mapped_column(String(200), nullable=False)
    business_type: Mapped[str | None] = mapped_column(String(120), nullable=True)
    industry: Mapped[str | None] = mapped_column(String(120), nullable=True)
    country: Mapped[str] = mapped_column(String(2), nullable=False, default="ZA")
    currency_code: Mapped[str] = mapped_column(String(3), nullable=False, default="ZAR")
    region: Mapped[str | None] = mapped_column(String(120), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )


class FinancialImport(Base):
    __tablename__ = "business_financial_imports"
    __table_args__ = (
        UniqueConstraint(
            "organization_id",
            "workspace_id",
            "content_hash",
            name="uq_business_financial_imports_workspace_hash",
        ),
        UniqueConstraint(
            "organization_id",
            "workspace_id",
            "id",
            name="uq_business_financial_imports_org_workspace_id",
        ),
        ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    organization_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    workspace_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    content_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    decimal_format: Mapped[str] = mapped_column(String(20), nullable=False)
    row_count: Mapped[int] = mapped_column(Integer, nullable=False)
    imported_count: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


class FinancialTransaction(Base):
    __tablename__ = "business_financial_transactions"
    __table_args__ = (
        CheckConstraint(
            "transaction_type IN ('revenue', 'expense')", name="valid_transaction_type"
        ),
        UniqueConstraint(
            "organization_id",
            "workspace_id",
            "fingerprint",
            name="uq_business_financial_transactions_workspace_fingerprint",
        ),
        ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
        ),
        ForeignKeyConstraint(
            ["organization_id", "workspace_id", "import_id"],
            [
                "business_financial_imports.organization_id",
                "business_financial_imports.workspace_id",
                "business_financial_imports.id",
            ],
        ),
        ForeignKeyConstraint(
            ["organization_id", "workspace_id", "business_profile_id"],
            [
                "business_profiles.organization_id",
                "business_profiles.workspace_id",
                "business_profiles.id",
            ],
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    organization_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    workspace_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    business_profile_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    import_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    transaction_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    transaction_type: Mapped[str] = mapped_column(String(20), nullable=False)
    category: Mapped[str] = mapped_column(String(120), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)
    source_reference: Mapped[str | None] = mapped_column(String(255), nullable=True)
    fingerprint: Mapped[str] = mapped_column(String(64), nullable=False)
    source_line: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


class BusinessAnalysis(Base):
    __tablename__ = "business_analyses"
    __table_args__ = (
        UniqueConstraint(
            "organization_id",
            "workspace_id",
            "id",
            name="uq_business_analyses_org_workspace_id",
        ),
        ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
        ),
        ForeignKeyConstraint(
            ["organization_id", "workspace_id", "business_profile_id"],
            [
                "business_profiles.organization_id",
                "business_profiles.workspace_id",
                "business_profiles.id",
            ],
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    organization_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    workspace_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    business_profile_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    question: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    ai_status: Mapped[str] = mapped_column(String(30), nullable=False)
    analysis_data: Mapped[dict[str, object]] = mapped_column(JSON, nullable=False)
    evidence_data: Mapped[list[dict[str, object]]] = mapped_column(JSON, nullable=False)
    model_metadata: Mapped[dict[str, str | None] | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


class BusinessAction(Base):
    __tablename__ = "business_actions"
    __table_args__ = (
        CheckConstraint(
            "status IN ('open', 'in_progress', 'completed', 'cancelled')",
            name="valid_status",
        ),
        CheckConstraint("priority IN ('low', 'medium', 'high')", name="valid_priority"),
        CheckConstraint(
            "external_execution_status = 'not_executed'",
            name="internal_tracking_only",
        ),
        ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
        ),
        ForeignKeyConstraint(
            ["organization_id", "workspace_id", "analysis_id"],
            [
                "business_analyses.organization_id",
                "business_analyses.workspace_id",
                "business_analyses.id",
            ],
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    organization_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    workspace_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    analysis_id: Mapped[UUID] = mapped_column(Uuid, nullable=False, index=True)
    source_insight_id: Mapped[str] = mapped_column(String(120), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)
    reason: Mapped[str] = mapped_column(String(2000), nullable=False)
    priority: Mapped[str] = mapped_column(String(20), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="open")
    outcome: Mapped[str | None] = mapped_column(String(2000), nullable=True)
    external_execution_status: Mapped[str] = mapped_column(
        String(30), nullable=False, default="not_executed"
    )
    supporting_evidence: Mapped[list[dict[str, object]]] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
