# JobPilot AI

## Vision

JobPilot AI is a fully autonomous AI-powered job application assistant.

It continuously searches multiple job portals, analyzes job descriptions, evaluates ATS compatibility, generates optimized resumes, applies to suitable jobs, tracks every application, and provides analytics through a modern dashboard.

---

# Goals

- Reduce manual job searching
- Improve ATS score
- Generate optimized resumes
- Automatically apply for suitable jobs
- Track every application
- Provide analytics
- Notify users instantly

---

# Core Features

## Job Search

- LinkedIn
- Indeed
- Naukri
- Wellfound
- Company Career Pages

---

## AI Agents

### Search Agent

Searches job portals.

---

### JD Parser Agent

Extracts

- Skills
- Responsibilities
- Experience
- Salary
- Location

---

### ATS Agent

Calculates

- Keyword Match
- Skill Match
- Experience Match
- Certification Match

Returns a Job Fit Score.

---

### Resume Agent

Generates ATS-optimized resumes.

---

### Apply Agent

Uses browser automation to apply.

---

### Notification Agent

Sends

- Telegram
- Email

notifications.

---

### Analytics Agent

Creates reports

- Applications
- Interviews
- Rejections
- Salary Trends

---

# Dashboard

- Total Jobs Found
- Applied Jobs
- Pending
- Rejected
- Interviews
- Highest Salary
- Average ATS Score

---

# Database

Users

Jobs

Applications

Resumes

Notifications

Settings

---

# Tech Stack

Frontend

- Next.js
- TypeScript
- Tailwind

Backend

- FastAPI

Database

- SQLite
- PostgreSQL (Future)

AI

- Ollama
- LangGraph

Automation

- Playwright

Notifications

- Telegram

Deployment

- Docker

---

# Roadmap

Sprint 1

✅ Project Setup

Sprint 2

⬜ Configuration
⬜ Logging
⬜ Database

Sprint 3

⬜ Authentication

Sprint 4

⬜ Job Search Agent

Sprint 5

⬜ JD Parser

Sprint 6

⬜ ATS Engine

Sprint 7

⬜ Resume Generator

Sprint 8

⬜ Browser Automation

Sprint 9

⬜ Notifications

Sprint 10

⬜ Dashboard

Sprint 11

⬜ Analytics

Sprint 12

⬜ Production Deployment

---

# Coding Standards

- Type hints everywhere
- Docstrings
- Repository Pattern
- Service Layer
- SOLID Principles
- Clean Architecture
- Unit Tests

---

# Success Criteria

A user uploads a resume once.

The AI automatically

- finds jobs
- evaluates compatibility
- optimizes the resume
- applies (where supported)
- logs applications
- notifies the user
- tracks progress