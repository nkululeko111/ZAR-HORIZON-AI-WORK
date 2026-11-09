import asyncio

from httpx import ASGITransport, AsyncClient
from zar_horizon_api.main import app


async def request(path: str) -> tuple[int, dict[str, str]]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get(path)
    return response.status_code, response.json()


def test_health_endpoint() -> None:
    status_code, body = asyncio.run(request("/health"))

    assert status_code == 200
    assert body == {"status": "ok"}


def test_version_endpoint() -> None:
    status_code, body = asyncio.run(request("/api/v1/version"))

    assert status_code == 200
    assert body["version"] == "0.1.0"
