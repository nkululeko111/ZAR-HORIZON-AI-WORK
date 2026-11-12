from functools import lru_cache
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ZAR HORIZON AI @WORK API"
    app_env: str = "development"
    app_version: str = "0.1.0"
    log_level: str = "INFO"
    database_url: str = "postgresql+psycopg://localhost/zar_horizon"
    business_partner_local_mode: bool = False
    business_partner_ai_api_key: SecretStr | None = None
    business_partner_ai_chat_completions_url: str | None = None
    business_partner_ai_provider: str | None = None
    business_partner_ai_model: str | None = None
    business_partner_ai_model_version: str | None = None
    business_partner_ai_model_source: str | None = None
    business_partner_ai_model_license: str | None = None
    business_partner_ai_model_license_type: Literal[
        "open_source", "open_weights", "restricted", "unknown"
    ] = "unknown"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
