# Architecture Decisions

## Decision 001

Date: 2026-07-20

### Decision

Backend uses FastAPI.

### Reason

- Excellent API support
- Automatic Swagger documentation
- High performance
- Strong Python ecosystem

---

## Decision 002

Frontend uses Next.js.

### Reason

- Modern React framework
- TypeScript support
- App Router
- Tailwind integration

---

## Decision 003

Architecture

Repository Pattern + Service Layer.

### Reason

Keeps business logic independent from API and database.

---

## Decision 004

Database

SQLite during development.

PostgreSQL in production.

### Reason

SQLite is simple and requires zero setup during development.

---

## Decision 005

AI

Local-first using Ollama whenever possible.

Cloud LLMs can be added later.