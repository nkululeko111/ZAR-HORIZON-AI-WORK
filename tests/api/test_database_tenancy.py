from sqlalchemy import ForeignKeyConstraint
from zar_horizon_api import models  # noqa: F401
from zar_horizon_api.database.base import Base


def test_agent_records_reference_workspaces_within_their_organization() -> None:
    for table_name in ("agent_sessions", "audit_events"):
        table = Base.metadata.tables[table_name]
        workspace_foreign_key = next(
            constraint
            for constraint in table.constraints
            if isinstance(constraint, ForeignKeyConstraint)
            and constraint.elements[0].column.table.name == "workspaces"
        )

        assert [element.parent.name for element in workspace_foreign_key.elements] == [
            "organization_id",
            "workspace_id",
        ]
        assert [element.column.name for element in workspace_foreign_key.elements] == [
            "organization_id",
            "id",
        ]


def test_business_partner_records_use_organization_scoped_workspace_foreign_keys() -> None:
    for table_name in (
        "business_profiles",
        "business_financial_imports",
        "business_financial_transactions",
        "business_analyses",
        "business_actions",
    ):
        table = Base.metadata.tables[table_name]
        workspace_foreign_key = next(
            constraint
            for constraint in table.constraints
            if isinstance(constraint, ForeignKeyConstraint)
            and constraint.elements[0].column.table.name == "workspaces"
        )

        assert [element.parent.name for element in workspace_foreign_key.elements] == [
            "organization_id",
            "workspace_id",
        ]
        assert [element.column.name for element in workspace_foreign_key.elements] == [
            "organization_id",
            "id",
        ]

    transactions = Base.metadata.tables["business_financial_transactions"]
    profile_foreign_key = next(
        constraint
        for constraint in transactions.constraints
        if isinstance(constraint, ForeignKeyConstraint)
        and constraint.elements[0].column.table.name == "business_profiles"
    )
    assert [element.parent.name for element in profile_foreign_key.elements] == [
        "organization_id",
        "workspace_id",
        "business_profile_id",
    ]
