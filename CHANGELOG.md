# Changelog

All notable changes to JobPilot AI will be documented here.

---

# Sprint 1 - Project Initialization

**Status:** ✅ Completed

**Start Date:** 2026-07-20

## Objectives

- Initialize project
- Setup backend
- Setup frontend
- Configure Git
- Push project to GitHub

---

## Completed

### Backend

- Created FastAPI project
- Configured Uvicorn
- Added Swagger UI
- Created modular backend folder structure
- Created agent folders
- Created API structure
- Created services
- Created repositories
- Created schemas
- Created models
- Added prompts directory
- Added utilities
- Added workers

---

### Frontend

- Created Next.js project
- Enabled TypeScript
- Enabled Tailwind CSS
- Enabled App Router

---

### Project

- Created Git repository
- Connected GitHub repository
- Configured .gitignore
- Created documentation structure
- Created scripts directory

---

## Repository

GitHub

https://github.com/BalamuruganS-Data/jobpilot-ai

---

## Deliverables

- FastAPI backend
- Next.js frontend
- Swagger UI
- GitHub repository
- Initial architecture

---

## Lessons Learned

- Difference between local Git and GitHub
- GitHub authentication using GitHub CLI
- Importance of .gitignore
- FastAPI application structure
- Next.js project initialization

---

## Result

Sprint 1 completed successfully.

Ready for Sprint 2.

## [0.2.0] - 2026-07-21

### Added
- Centralized configuration using pydantic-settings
- Structured logging
- SQLAlchemy integration
- SQLite database
- Database session management
- Job model
- Automatic database initialization

# Changelog

All notable changes to JobPilot AI are documented here.

---

## Sprint 2 - Backend Foundation & ATS API (2026-07-23)

### Added

- Centralized application configuration using Pydantic Settings
- Environment variable support (.env)
- Structured logging across the application
- SQLite database integration
- SQLAlchemy ORM setup
- Automatic database initialization during application startup
- Job model and Resume model
- Jobs CRUD API
- Resume Upload API
- ATS Scoring API
- Swagger/OpenAPI documentation
- Clean project architecture (API, Services, Models, Schemas)

### Improved

- Startup lifecycle using FastAPI lifespan
- Database initialization process
- Project folder organization
- API versioning (/api/v1)

### Fixed

- Circular import issue between Base and Job model
- Uvicorn module loading issue
- Router registration issues preventing ATS endpoint from appearing