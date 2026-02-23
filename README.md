# CivicStack 🚀

![Build Status](https://img.shields.io/badge/build-in_progress-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![Backend](https://img.shields.io/badge/backend-FastAPI-blue)
![Frontend](https://img.shields.io/badge/frontend-React-blue)
![Database](https://img.shields.io/badge/database-PostgreSQL-blue)
![Open Source](https://img.shields.io/badge/open_source-yes-brightgreen)

**Team:** Harshal Chavan & Team  
**Demo Video (unlisted):** https://youtu.be/YOUR_DEMO_LINK  
**Live (staging):** https://staging.civicstack.example.com  *(replace when ready)*  
**Repo:** https://github.com/YOUR-GITHUB-USERNAME/civicstack

---

## TL;DR
CivicStack is an open-source civic issue reporting and transparency platform that enables citizens to submit geo-tagged reports (potholes, drainage, streetlights, sanitation), empowers municipal triage, and publishes open data exports. Designed for reproducibility, privacy, and real-world pilots.

---

## Why CivicStack?
- **Impact-first:** Designed to close the loop from citizen report → municipal triage → public transparency.  
- **Reproducible:** Docker + reproducible deployments; Cloud-ready (GCP / Render / Railway).  
- **Open:** MIT licensed, accepts contributions, partner-friendly export (CSV/JSON/CKAN).

---

## MVP Feature Set (March deliverables)
1. Map-based report submission (title, category, photo, location)  
2. Public dashboard (map + list + filters)  
3. Admin triage panel (status, notes, assign agency)  
4. Export endpoints (CSV / JSON) + tracking IDs for provenance  
5. Reproducible `docker-compose` demo and staging deploy

---

## Tech stack
- Frontend: React, Tailwind CSS, Leaflet (OpenStreetMap)  
- Backend: FastAPI, SQLAlchemy, PostgreSQL  
- Storage: Supabase Storage / Cloud Storage (optional)  
- Deployment: Docker Compose (local), Cloud Run / Render / GCP (staging/prod)

---

## Quickstart (local, demo-ready)
1. Clone:
```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/civicstack.git
cd civicstack
```
2. Copy `.env.example` to `.env` and set values (DATABASE_URL, ADMIN_PASS).
3. Start with Docker Compose:
```bash
docker-compose up --build
```
4. Backend: http://localhost:8000  → `/health`, `/api/v1/issues`  
   Frontend: http://localhost:3000

---

## March Roadmap (public, commits visible)
- **Week 1 (Mar 1–7):** Backend models, endpoints, seed script, tests.  
- **Week 2 (Mar 8–14):** Frontend map UI, submit flow, marker rendering.  
- **Week 3 (Mar 15–21):** Admin panel, CSV/JSON export, privacy & consent.  
- **Week 4 (Mar 22–27):** Polish, staging deploy, QA, demo video record.

---

## How we prove impact (what judges will check)
- Public GitHub commit history throughout March  
- Reproducible Docker demo and staged live URL  
- Demo video (≤3 minutes) + README docs  
- Exportable dataset + tracking IDs

---

## Contributing
1. Fork → create branch `feature/...` → open PR  
2. Follow code style, write tests, include meaningful commit messages  
3. Label small tasks as `good first issue` to onboard contributors

---

## Contact
Harshal Chavan — harshal@example.com  
