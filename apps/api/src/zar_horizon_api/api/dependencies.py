from collections.abc import Generator
from dataclasses import dataclass
from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from zar_horizon_api.core.config import Settings, get_settings
from zar_horizon_api.database.session import SessionLocal
from zar_horizon_api.models.platform import Organization, Workspace

LOCAL_ORGANIZATION_ID = UUID("5e5f9794-8fd1-4fd9-8ed2-257df8de0ab1")
LOCAL_WORKSPACE_ID = UUID("5e5f9794-8fd1-4fd9-8ed2-257df8de0ab2")


@dataclass(frozen=True)
class BusinessPartnerContext:
    organization_id: UUID
    workspace_id: UUID


def get_db() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_business_partner_context(
    db: Annotated[Session, Depends(get_db)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> BusinessPartnerContext:
    if not settings.business_partner_local_mode or settings.app_env.lower() not in {
        "development",
        "test",
    }:
        raise HTTPException(
            status_code=404,
            detail="The local Business Partner workspace is disabled in this environment.",
        )

    organization = db.get(Organization, LOCAL_ORGANIZATION_ID)
    if organization is None:
        organization = Organization(
            id=LOCAL_ORGANIZATION_ID,
            name="Local Business Partner (Development)",
        )
        db.add(organization)

    workspace = db.get(Workspace, LOCAL_WORKSPACE_ID)
    if workspace is None:
        workspace = Workspace(
            id=LOCAL_WORKSPACE_ID,
            organization_id=LOCAL_ORGANIZATION_ID,
            name="Local Business Partner",
        )
        db.add(workspace)
    elif workspace.organization_id != LOCAL_ORGANIZATION_ID:
        raise HTTPException(
            status_code=503,
            detail="The configured local workspace has an invalid organisation relationship.",
        )

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        organization = db.get(Organization, LOCAL_ORGANIZATION_ID)
        workspace = db.get(Workspace, LOCAL_WORKSPACE_ID)
        if organization is None or workspace is None:
            raise HTTPException(
                status_code=503,
                detail="The local Business Partner workspace could not be initialized.",
            ) from exc
        if workspace.organization_id != organization.id:
            raise HTTPException(
                status_code=503,
                detail="The local workspace has an invalid organisation relationship.",
            ) from exc

    return BusinessPartnerContext(
        organization_id=LOCAL_ORGANIZATION_ID,
        workspace_id=LOCAL_WORKSPACE_ID,
    )
