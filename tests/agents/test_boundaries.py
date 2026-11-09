from zar_horizon_business_partner.service import health_status as business_status
from zar_horizon_business_partner.service import permitted_tools as business_tools
from zar_horizon_hacker.service import health_status as hacker_status
from zar_horizon_hacker.service import permitted_tools as hacker_tools


def test_agent_scaffolds_are_separate_and_have_no_enabled_tools() -> None:
    assert business_status()["service"] == "business-partner"
    assert hacker_status()["service"] == "hacker"
    assert business_tools() == frozenset()
    assert hacker_tools() == frozenset()
