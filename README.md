# Digital Public Grievance + Welfare + Governance Super-App (Prototype)

This repository contains a Python/Flask prototype for the multi-role governance platform described in `requirements.md` and `design.md`. It includes a shared backend with blueprints for the Citizen App, Government Entity App, and Politician Dashboard.

## Full Development Process (High-Level)

1. **Plan & Scope**
   - Confirm requirements, acceptance criteria, and language support.
   - Define MVP scope (Citizen App) before expanding to government and politician modules.

2. **Architecture & Data Design**
   - Establish multi-database architecture: PostgreSQL, Redis, Vector DB.
   - Define core data models and service interfaces.
   - Map AI agent responsibilities and integration points.

3. **Project Foundation**
   - Create Flask app with blueprints per role.
   - Configure settings, logging, and environment variables.
   - Set up internationalization (Flask-Babel).

4. **Security & Compliance Baseline**
   - Encrypt PII at rest and in transit.
   - Establish audit logging and role-based access control.

5. **Feature Build-Out (Phased)**
   - Phase 1: Citizen App modules (complaints, emergency, schemes, certificates).
   - Phase 2: Government Entity complaint queue + SLA workflows.
   - Phase 3: Politician analytics dashboards and insights.

6. **Testing Strategy**
   - Unit tests for services and data handling.
   - Property-based tests for the correctness properties in `design.md`.

7. **Deployment & Observability**
   - Configure production environments, monitoring, and logging.
   - Automate CI/CD pipeline for deployments.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Visit `http://localhost:5000` in your browser.

## AI Complaint Draft (Prototype)

The citizen complaint form includes a lightweight AI draft helper that:
- Suggests a category and department.
- Generates a formal complaint preview based on user input.

This is a placeholder for a future LLM-powered workflow.

## Project Structure

```
app/
  __init__.py
  config.py
  extensions.py
  services/
    complaint_ai.py
  blueprints/
    core/
    citizen/
    government/
    politician/
  templates/
    core/
    citizen/
    government/
    politician/
run.py
requirements.txt
```

## Next Steps

- Add SQLAlchemy models for users, complaints, and schemes.
- Implement Aadhaar/DigiLocker mock integrations.
- Build AI agent service layer and vector database connector.
- Add tests for properties outlined in `design.md`.
