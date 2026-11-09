from pydantic_settings import BaseSettings, SettingsConfigDict


class BusinessPartnerSettings(BaseSettings):
    service_name: str = "business-partner"
    environment: str = "development"

    model_config = SettingsConfigDict(env_prefix="BUSINESS_PARTNER_", extra="ignore")
