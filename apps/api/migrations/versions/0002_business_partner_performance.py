"""Add development Business Partner performance workflow tables."""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision = "0002_business_partner_performance"
down_revision = "0001_platform_foundation"
branch_labels = None
depends_on = None

UUID = postgresql.UUID(as_uuid=True)


def upgrade() -> None:
    op.create_table(
        "business_profiles",
        sa.Column("id", UUID, nullable=False),
        sa.Column("organization_id", UUID, nullable=False),
        sa.Column("workspace_id", UUID, nullable=False),
        sa.Column("business_name", sa.String(length=200), nullable=False),
        sa.Column("business_type", sa.String(length=120), nullable=True),
        sa.Column("industry", sa.String(length=120), nullable=True),
        sa.Column("country", sa.String(length=2), nullable=False),
        sa.Column("currency_code", sa.String(length=3), nullable=False),
        sa.Column("region", sa.String(length=120), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
            name=op.f("fk_business_profiles_organization_id_workspaces"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_business_profiles")),
        sa.UniqueConstraint(
            "organization_id", "workspace_id", name="uq_business_profiles_workspace"
        ),
        sa.UniqueConstraint(
            "organization_id",
            "workspace_id",
            "id",
            name="uq_business_profiles_org_workspace_id",
        ),
    )
    op.create_index(
        op.f("ix_business_profiles_organization_id"),
        "business_profiles",
        ["organization_id"],
    )
    op.create_index(
        op.f("ix_business_profiles_workspace_id"), "business_profiles", ["workspace_id"]
    )

    op.create_table(
        "business_financial_imports",
        sa.Column("id", UUID, nullable=False),
        sa.Column("organization_id", UUID, nullable=False),
        sa.Column("workspace_id", UUID, nullable=False),
        sa.Column("content_hash", sa.String(length=64), nullable=False),
        sa.Column("file_name", sa.String(length=255), nullable=False),
        sa.Column("decimal_format", sa.String(length=20), nullable=False),
        sa.Column("row_count", sa.Integer(), nullable=False),
        sa.Column("imported_count", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
            name=op.f("fk_business_financial_imports_organization_id_workspaces"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_business_financial_imports")),
        sa.UniqueConstraint(
            "organization_id",
            "workspace_id",
            "content_hash",
            name="uq_business_financial_imports_workspace_hash",
        ),
        sa.UniqueConstraint(
            "organization_id",
            "workspace_id",
            "id",
            name="uq_business_financial_imports_org_workspace_id",
        ),
    )
    op.create_index(
        op.f("ix_business_financial_imports_organization_id"),
        "business_financial_imports",
        ["organization_id"],
    )
    op.create_index(
        op.f("ix_business_financial_imports_workspace_id"),
        "business_financial_imports",
        ["workspace_id"],
    )

    op.create_table(
        "business_financial_transactions",
        sa.Column("id", UUID, nullable=False),
        sa.Column("organization_id", UUID, nullable=False),
        sa.Column("workspace_id", UUID, nullable=False),
        sa.Column("business_profile_id", UUID, nullable=False),
        sa.Column("import_id", UUID, nullable=False),
        sa.Column("transaction_date", sa.Date(), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("transaction_type", sa.String(length=20), nullable=False),
        sa.Column("category", sa.String(length=120), nullable=False),
        sa.Column("amount", sa.Numeric(precision=18, scale=2), nullable=False),
        sa.Column("currency", sa.String(length=3), nullable=False),
        sa.Column("source_reference", sa.String(length=255), nullable=True),
        sa.Column("fingerprint", sa.String(length=64), nullable=False),
        sa.Column("source_line", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
            name=op.f("fk_business_financial_transactions_organization_id_workspaces"),
        ),
        sa.ForeignKeyConstraint(
            ["organization_id", "workspace_id", "import_id"],
            [
                "business_financial_imports.organization_id",
                "business_financial_imports.workspace_id",
                "business_financial_imports.id",
            ],
            name="fk_business_financial_transactions_import_workspace",
        ),
        sa.ForeignKeyConstraint(
            ["organization_id", "workspace_id", "business_profile_id"],
            [
                "business_profiles.organization_id",
                "business_profiles.workspace_id",
                "business_profiles.id",
            ],
            name="fk_business_financial_transactions_profile_workspace",
        ),
        sa.CheckConstraint(
            "transaction_type IN ('revenue', 'expense')",
            name=op.f("ck_business_financial_transactions_valid_transaction_type"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_business_financial_transactions")),
        sa.UniqueConstraint(
            "organization_id",
            "workspace_id",
            "fingerprint",
            name="uq_business_financial_transactions_workspace_fingerprint",
        ),
    )
    for column in (
        "organization_id",
        "workspace_id",
        "business_profile_id",
        "import_id",
        "transaction_date",
    ):
        op.create_index(
            op.f(f"ix_business_financial_transactions_{column}"),
            "business_financial_transactions",
            [column],
        )

    op.create_table(
        "business_analyses",
        sa.Column("id", UUID, nullable=False),
        sa.Column("organization_id", UUID, nullable=False),
        sa.Column("workspace_id", UUID, nullable=False),
        sa.Column("business_profile_id", UUID, nullable=False),
        sa.Column("question", sa.String(length=1000), nullable=True),
        sa.Column("ai_status", sa.String(length=30), nullable=False),
        sa.Column("analysis_data", sa.JSON(), nullable=False),
        sa.Column("evidence_data", sa.JSON(), nullable=False),
        sa.Column("model_metadata", sa.JSON(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
            name=op.f("fk_business_analyses_organization_id_workspaces"),
        ),
        sa.ForeignKeyConstraint(
            ["organization_id", "workspace_id", "business_profile_id"],
            [
                "business_profiles.organization_id",
                "business_profiles.workspace_id",
                "business_profiles.id",
            ],
            name="fk_business_analyses_profile_workspace",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_business_analyses")),
        sa.UniqueConstraint(
            "organization_id",
            "workspace_id",
            "id",
            name="uq_business_analyses_org_workspace_id",
        ),
    )
    for column in ("organization_id", "workspace_id", "business_profile_id"):
        op.create_index(
            op.f(f"ix_business_analyses_{column}"),
            "business_analyses",
            [column],
        )

    op.create_table(
        "business_actions",
        sa.Column("id", UUID, nullable=False),
        sa.Column("organization_id", UUID, nullable=False),
        sa.Column("workspace_id", UUID, nullable=False),
        sa.Column("analysis_id", UUID, nullable=False),
        sa.Column("source_insight_id", sa.String(length=120), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(length=2000), nullable=False),
        sa.Column("reason", sa.String(length=2000), nullable=False),
        sa.Column("priority", sa.String(length=20), nullable=False),
        sa.Column("status", sa.String(length=20), server_default="open", nullable=False),
        sa.Column("outcome", sa.String(length=2000), nullable=True),
        sa.Column(
            "external_execution_status",
            sa.String(length=30),
            server_default="not_executed",
            nullable=False,
        ),
        sa.Column("supporting_evidence", sa.JSON(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["organization_id", "workspace_id"],
            ["workspaces.organization_id", "workspaces.id"],
            name=op.f("fk_business_actions_organization_id_workspaces"),
        ),
        sa.ForeignKeyConstraint(
            ["organization_id", "workspace_id", "analysis_id"],
            [
                "business_analyses.organization_id",
                "business_analyses.workspace_id",
                "business_analyses.id",
            ],
            name="fk_business_actions_analysis_workspace",
        ),
        sa.CheckConstraint(
            "status IN ('open', 'in_progress', 'completed', 'cancelled')",
            name=op.f("ck_business_actions_valid_status"),
        ),
        sa.CheckConstraint(
            "priority IN ('low', 'medium', 'high')",
            name=op.f("ck_business_actions_valid_priority"),
        ),
        sa.CheckConstraint(
            "external_execution_status = 'not_executed'",
            name=op.f("ck_business_actions_internal_tracking_only"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_business_actions")),
    )
    for column in ("organization_id", "workspace_id", "analysis_id"):
        op.create_index(op.f(f"ix_business_actions_{column}"), "business_actions", [column])


def downgrade() -> None:
    for column in ("analysis_id", "workspace_id", "organization_id"):
        op.drop_index(op.f(f"ix_business_actions_{column}"), table_name="business_actions")
    op.drop_table("business_actions")
    for column in ("business_profile_id", "workspace_id", "organization_id"):
        op.drop_index(op.f(f"ix_business_analyses_{column}"), table_name="business_analyses")
    op.drop_table("business_analyses")
    for column in (
        "transaction_date",
        "import_id",
        "business_profile_id",
        "workspace_id",
        "organization_id",
    ):
        op.drop_index(
            op.f(f"ix_business_financial_transactions_{column}"),
            table_name="business_financial_transactions",
        )
    op.drop_table("business_financial_transactions")
    for column in ("workspace_id", "organization_id"):
        op.drop_index(
            op.f(f"ix_business_financial_imports_{column}"),
            table_name="business_financial_imports",
        )
    op.drop_table("business_financial_imports")
    for column in ("workspace_id", "organization_id"):
        op.drop_index(op.f(f"ix_business_profiles_{column}"), table_name="business_profiles")
    op.drop_table("business_profiles")
