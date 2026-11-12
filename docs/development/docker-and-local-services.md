# Docker and local services

## 1. Purpose

This document reviews the existing Docker and local infrastructure setup and defines the minimal, practical configuration for the repository as it stands today.

## 2. Existing configuration assessment

The repository already contains a `docker-compose.yml` file with:

- PostgreSQL 17 container
- API service container
- web service container
- named volume for persistent database storage
- health checks for PostgreSQL

This configuration is appropriate for the current architecture and does not add unnecessary infrastructure.

## 3. Local services included

### PostgreSQL

PostgreSQL is the only persistent service required for the current local stack.

Requirements already present:

- named volume for persistence
- health checks
- service name `db`
- environment-based database configuration

## 4. Service boundaries

The current Compose setup is deliberately minimal:

- `db` for persistent data
- `api` for the FastAPI service
- `web` for the Next.js frontend

This aligns with the repository’s current architecture and avoids introducing infrastructure that the project does not yet require.

## 5. What is not included

The project should not add infrastructure such as:

- Redis
- Kafka
- RabbitMQ
- Elasticsearch
- vector database
- Kubernetes manifests

These should be added only when actual product or technical requirements are identified and justified by the implemented application.

## 6. Guidance for local development

Use Compose to start the local database and application stack when a full environment is needed.

Recommended commands:

```powershell
docker compose up --build db api
# or

docker compose up --build
```

Stop with:

```powershell
docker compose down
```

Use `docker compose down -v` only when the developer intentionally wants to delete the local database volume.

## 7. Security and hygiene

- do not store live credentials in Compose files,
- use `.env` or environment injection for secrets,
- avoid over-exposing the database port outside local development,
- ensure that Docker configuration remains local-only and not production-oriented by default.

## 8. Conclusion

The current Docker approach is already a good fit for the repository. It is minimal, clear, and consistent with the current architecture. The recommended improvement is to document the exact purpose and limits of the Compose configuration rather than expanding the stack prematurely.
