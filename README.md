# DevOps Platform

Production-like backend platform built for learning DevOps, backend engineering, CI/CD, and infrastructure practices.

---

# Stack

## Backend

* FastAPI
* SQLAlchemy
* Alembic
* Pydantic
* Pytest

## Infrastructure

* Docker
* Docker Compose
* PostgreSQL
* Redis

## CI/CD & Tooling

* GitHub Actions
* Ruff
* Black
* pre-commit

---

# Live Demo

API Documentation:

```text
https://api.vzhyhalau-devops.uk/docs
```

---

# Features

* Containerized FastAPI application
* PostgreSQL integration
* Redis integration
* SQLAlchemy ORM models
* Alembic database migrations
* CRUD API
* Healthcheck endpoints
* Automated tests with pytest
* GitHub Actions CI pipeline
* Ruff + Black linting/formatting
* pre-commit hooks
* Environment-based configuration

---

# Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── backend-ci.yml
│
├── backend/
│   ├── alembic/
│   │   ├── versions/
│   │   └── env.py
│   │
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── health.py
│   │   │       └── users.py
│   │   │
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── db/
│   │   │   ├── connections.py
│   │   │   ├── database.py
│   │   │   └── session.py
│   │   │
│   │   ├── models/
│   │   │   └── user.py
│   │   │
│   │   ├── schemas/
│   │   │   └── user.py
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   │   └── test_users.py
│   │
│   ├── Dockerfile
│   ├── alembic.ini
│   └── requirements.txt
│
├── docker-compose.yml
├── Makefile
├── pyproject.toml
├── .pre-commit-config.yaml
├── .env.example
└── README.md
```

---

# Getting Started

## Requirements

* Docker
* Docker Compose
* Git
* Python 3.12+ (optional for local tooling)

---

# Environment Variables

Create `.env` file in the project root:

```env
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpassword
POSTGRES_DB=devdb

DATABASE_URL=postgresql://devuser:devpassword@postgres:5432/devdb
REDIS_URL=redis://redis:6379
```

---

# Run Application

## Build and start services

```bash
make build
```

or:

```bash
docker compose up --build
```

---

# Stop Services

```bash
make down
```

---

# Restart Services

```bash
make restart
```

---

# View Logs

```bash
make logs
```

---

# API Documentation

FastAPI Swagger UI:

```text
http://localhost:8000/docs
```

---

# Healthcheck Endpoint

```text
GET /health
```

Example response:

```json
{
  "api": "healthy",
  "postgres": "connected",
  "redis": "connected"
}
```

---

# Database Migrations

## Create migration

```bash
docker compose exec backend alembic revision --autogenerate -m "migration_name"
```

## Apply migrations

```bash
docker compose exec backend alembic upgrade head
```

---

# Run Tests

```bash
docker compose exec backend pytest
```

---

# Linting & Formatting

## Ruff

```bash
ruff check backend
```

## Auto-fix

```bash
ruff check backend --fix
```

## Format

```bash
ruff format backend
black backend
```

---

# Pre-commit Hooks

Install hooks:

```bash
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```

---

# CI/CD Pipeline

Current deployment flow:

```text
git push
→ GitHub Actions
→ Ruff / Black checks
→ Docker image build
→ Push image to GHCR
→ SSH deploy to VPS
→ Pull latest image
→ Restart containers
→ Run Alembic migrations
```

---

# Infrastructure

Production infrastructure:

* Ubuntu 24.04 VPS
* Traefik reverse proxy
* Automatic HTTPS via Let's Encrypt
* GitHub Container Registry
* Docker Compose production stack
* Automated deployments via GitHub Actions

---

# CI Pipeline

GitHub Actions pipeline includes:

* Ruff linting
* Black formatting checks
* Pytest execution
* Syntax validation
* Docker image build

---

# Learning Goals

This project is focused on learning:

* DevOps practices
* Containerization
* CI/CD pipelines
* Backend engineering
* Database migrations
* Infrastructure orchestration
* Testing workflows
* Production-like architecture

---

# Current Production Stack

```text
Internet
    ↓
Cloudflare DNS
    ↓
Traefik
    ↓
FastAPI Backend
    ↓
PostgreSQL / Redis
```

---

# Planned Improvements

* GitHub Container Registry
* Traefik reverse proxy
* HTTPS
* Kubernetes deployment
* Terraform infrastructure
* Prometheus metrics
* Grafana dashboards
* Loki logging
* JWT authentication
* Async SQLAlchemy
* Background workers

---

# License

MIT
