from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import listings, calculator

app = FastAPI(
    title="Affordable Housing Finder API",
    description="API for finding affordable housing for new graduates",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(listings.router, prefix="/api/listings", tags=["Listings"])
app.include_router(calculator.router, prefix="/api/calculator", tags=["Calculator"])

@app.get("/")
async def root():
    return {"message": "Affordable Housing Finder API", "status": "running", "docs": "/docs"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
