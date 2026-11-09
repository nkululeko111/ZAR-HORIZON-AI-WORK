from zar_horizon_business_partner.config import BusinessPartnerSettings
from zar_horizon_business_partner.tools import ALLOWED_TOOLS


def health_status() -> dict[str, str]:
    return {"service": BusinessPartnerSettings().service_name, "status": "scaffold"}


def run_agent() -> None:
    raise NotImplementedError("Business Partner orchestration has not been implemented.")


def permitted_tools() -> frozenset[str]:
    return ALLOWED_TOOLS
