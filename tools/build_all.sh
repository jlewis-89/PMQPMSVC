#!/usr/bin/env bash
set -e
echo "Building frontend (web) and backend (API) in parallel..."
(cd frontend && npm ci && npm run build) &
(cd backend && python -m venv venv || true && source venv/Scripts/activate && pip install -r requirements.txt) &
wait
echo "Build complete. You can run frontend and backend separately for dev:"
echo "  - Frontend: cd frontend && npm start"
echo "  - Backend: cd backend && uvicorn main:app --reload"
