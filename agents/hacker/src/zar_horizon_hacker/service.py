from zar_horizon_hacker.config import HackerSettings
from zar_horizon_hacker.tools import ALLOWED_TOOLS


def health_status() -> dict[str, str]:
    return {"service": HackerSettings().service_name, "status": "scaffold"}


def run_agent() -> None:
    raise NotImplementedError("Hacker orchestration has not been implemented.")


def permitted_tools() -> frozenset[str]:
    return ALLOWED_TOOLS
