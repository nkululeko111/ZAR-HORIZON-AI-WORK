import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from zar_horizon_api.api.routes import health, version
from zar_horizon_api.core.config import get_settings
from zar_horizon_api.core.logging import configure_logging

settings = get_settings()
configure_logging(settings.log_level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("API starting", extra={"environment": settings.app_env})
    yield
    logger.info("API stopped")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Shared platform API foundation.",
    lifespan=lifespan,
)
app.include_router(health.router)
app.include_router(version.router)
