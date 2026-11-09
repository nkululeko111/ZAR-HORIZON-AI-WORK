FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /bin/
WORKDIR /workspace
COPY pyproject.toml uv.lock ./
COPY apps/api ./apps/api
COPY agents ./agents
RUN uv sync --frozen --package zar-horizon-api --no-dev

EXPOSE 8000
CMD ["uv", "run", "--frozen", "--package", "zar-horizon-api", "uvicorn", "zar_horizon_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
