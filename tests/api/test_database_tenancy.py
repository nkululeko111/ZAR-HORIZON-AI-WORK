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
