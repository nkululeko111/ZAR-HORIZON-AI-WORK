from typing import Annotated

from fastapi import APIRouter, Depends

from zar_horizon_api.core.config import Settings, get_settings

router = APIRouter(prefix="/api/v1", tags=["version"])


@router.get("/version")
def version(settings: Annotated[Settings, Depends(get_settings)]) -> dict[str, str]:
    return {"name": settings.app_name, "version": settings.app_version}
