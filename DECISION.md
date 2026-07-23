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

## Decision 006

Date: 2026-07-20

### Decision

The project will follow an Agile sprint-based development process.

### Reason

Large AI systems are easier to build, review, test, and maintain when work is delivered in small iterations.

Every sprint must include:

- Planning
- Implementation
- Testing
- Documentation
- Git commit
- Sprint review

## Decision 007

Date: 2026-07-21

### Decision

Adopt SQLAlchemy ORM with SQLite for the initial development phase.

### Reason

- Zero-cost setup
- Easy local development
- ORM allows switching to PostgreSQL later with minimal code changes.

---

# Sprint 2 Technical Decisions

## Architecture

We continue following a layered architecture.

```
API
↓
Services
↓
Database
```

Business logic must remain inside Services.

Routes should only receive requests and return responses.

---

## Database

Chosen Database:
- SQLite

Reason:
- Zero configuration
- Easy development
- Easy migration to PostgreSQL later

---

## ORM

Chosen ORM:
- SQLAlchemy

Reason:
- Industry standard
- Easy migration
- Strong FastAPI integration

---

## API Design

Versioning:
```
/api/v1
```

Reason:
Supports future API versions without breaking existing clients.

---

## Documentation

Swagger UI remains enabled throughout development.

Reason:
- Faster testing
- Easier debugging
- Automatic API documentation

---

## ATS Engine

Current Version:
Rule-based scoring.

Future Version:
LLM-assisted semantic scoring using AI.

Reason:
Rule-based implementation provides a deterministic MVP while AI can be integrated later without changing the API contract.

---

## Current Project Status

Sprint 1
- ✅ Project Setup

Sprint 2
- ✅ Backend Foundation
- ✅ Database
- ✅ Jobs CRUD
- ✅ Resume Upload API
- ✅ ATS API
- ⏳ Intelligent ATS scoring
- ⏳ Resume Parsing