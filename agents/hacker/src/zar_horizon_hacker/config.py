from pydantic_settings import BaseSettings, SettingsConfigDict


class HackerSettings(BaseSettings):
    service_name: str = "hacker"
    environment: str = "development"

    model_config = SettingsConfigDict(env_prefix="HACKER_", extra="ignore")
