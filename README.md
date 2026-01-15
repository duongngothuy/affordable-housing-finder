# Affordable Housing Finder

A full-stack web application helping new graduates find affordable housing based on their salary and location preferences.

## Live Demo

- **Frontend:** [your-vercel-url.vercel.app](https://your-vercel-url.vercel.app)
- **Backend API:** [your-render-url.onrender.com/docs](https://your-render-url.onrender.com/docs)

## Screenshots

<!-- Add screenshots here -->

## Features

- **Budget Calculator** - Calculate affordable rent using the 30% income rule
- **Housing Search** - Filter listings by city, price, bedrooms, and property type
- **Interactive Map** - View listings on a map with location markers
- **Financial Health Score** - Get personalized affordability recommendations

## Tech Stack

**Frontend:** Next.js 14, TypeScript, Tailwind CSS, Leaflet.js

**Backend:** Python, FastAPI, SQLAlchemy, SQLite

**Deployment:** Vercel (frontend), Render (backend)

## Local Development

```bash
# Backend
cd backend
pip install -r requirements.txt
python seed_data.py
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/listings` | Get all listings with optional filters |
| GET | `/api/listings/{id}` | Get a specific listing |
| POST | `/api/calculator/budget` | Calculate budget breakdown |

## Project Structure

```
├── frontend/          # Next.js application
│   ├── src/app/       # Pages (home, search, calculator, listing)
│   ├── src/components # Reusable UI components
│   └── src/lib/       # API client and utilities
│
└── backend/           # FastAPI application
    └── app/
        ├── routers/   # API endpoints
        ├── models/    # Database models
        └── schemas/   # Pydantic validation
```

---

Built for new grads
