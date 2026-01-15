from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routers import listings, calculator
from app.database import engine, SessionLocal
from app.models import Base, Listing


def seed_database():
    """Create tables and seed data on startup"""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Listing).first():
        db.close()
        return

    sample_listings = [
        {"title": "Modern Studio in Downtown", "description": "Bright studio apartment with city views", "address": "123 Main St", "city": "San Diego", "state": "CA", "zip_code": "92101", "latitude": 32.7157, "longitude": -117.1611, "price": 1450, "bedrooms": 0, "bathrooms": 1, "sqft": 450, "property_type": "apartment", "amenities": ["gym", "pool"], "images": []},
        {"title": "Cozy 1BR near UCSD", "description": "Walking distance to campus", "address": "456 La Jolla Village Dr", "city": "San Diego", "state": "CA", "zip_code": "92093", "latitude": 32.8801, "longitude": -117.2340, "price": 1800, "bedrooms": 1, "bathrooms": 1, "sqft": 650, "property_type": "apartment", "amenities": ["parking", "laundry"], "images": []},
        {"title": "Affordable Room in Shared House", "description": "Private room in a 4BR house", "address": "789 College Ave", "city": "San Diego", "state": "CA", "zip_code": "92115", "latitude": 32.7633, "longitude": -117.0701, "price": 850, "bedrooms": 1, "bathrooms": 1, "sqft": 200, "property_type": "room", "amenities": ["wifi", "parking"], "images": []},
        {"title": "Spacious 2BR Apartment", "description": "Recently renovated with modern appliances", "address": "321 Harbor Dr", "city": "San Diego", "state": "CA", "zip_code": "92101", "latitude": 32.7096, "longitude": -117.1637, "price": 2400, "bedrooms": 2, "bathrooms": 2, "sqft": 1000, "property_type": "apartment", "amenities": ["gym", "rooftop"], "images": []},
        {"title": "Budget-Friendly Studio", "description": "Great starter apartment for recent grads", "address": "555 El Cajon Blvd", "city": "San Diego", "state": "CA", "zip_code": "92115", "latitude": 32.7543, "longitude": -117.0854, "price": 1200, "bedrooms": 0, "bathrooms": 1, "sqft": 400, "property_type": "apartment", "amenities": ["laundry"], "images": []},
        {"title": "Tech Hub Loft", "description": "Industrial-style loft in downtown Austin", "address": "100 Congress Ave", "city": "Austin", "state": "TX", "zip_code": "78701", "latitude": 30.2672, "longitude": -97.7431, "price": 1650, "bedrooms": 1, "bathrooms": 1, "sqft": 750, "property_type": "loft", "amenities": ["gym", "rooftop"], "images": []},
        {"title": "Affordable Austin Studio", "description": "Perfect for UT grads starting their career", "address": "2500 Guadalupe St", "city": "Austin", "state": "TX", "zip_code": "78705", "latitude": 30.2914, "longitude": -97.7414, "price": 1100, "bedrooms": 0, "bathrooms": 1, "sqft": 380, "property_type": "apartment", "amenities": ["pool"], "images": []},
        {"title": "Seattle Starter Home", "description": "Cozy apartment near Amazon HQ", "address": "400 Pine St", "city": "Seattle", "state": "WA", "zip_code": "98101", "latitude": 47.6062, "longitude": -122.3321, "price": 1900, "bedrooms": 1, "bathrooms": 1, "sqft": 600, "property_type": "apartment", "amenities": ["gym", "concierge"], "images": []},
        {"title": "Denver Mountain View", "description": "Beautiful views of the Rockies", "address": "1600 California St", "city": "Denver", "state": "CO", "zip_code": "80202", "latitude": 39.7392, "longitude": -104.9903, "price": 1550, "bedrooms": 1, "bathrooms": 1, "sqft": 700, "property_type": "apartment", "amenities": ["gym", "rooftop"], "images": []},
        {"title": "Phoenix Budget Living", "description": "Affordable desert living with pool access", "address": "3300 N Central Ave", "city": "Phoenix", "state": "AZ", "zip_code": "85012", "latitude": 33.4484, "longitude": -112.0740, "price": 950, "bedrooms": 1, "bathrooms": 1, "sqft": 550, "property_type": "apartment", "amenities": ["pool", "gym"], "images": []},
        {"title": "Atlanta Entry-Level Apartment", "description": "Close to tech companies and transit", "address": "200 Peachtree St", "city": "Atlanta", "state": "GA", "zip_code": "30303", "latitude": 33.7490, "longitude": -84.3880, "price": 1350, "bedrooms": 1, "bathrooms": 1, "sqft": 620, "property_type": "apartment", "amenities": ["gym", "pool"], "images": []},
        {"title": "Raleigh New Grad Special", "description": "Near Research Triangle Park tech hub", "address": "500 Fayetteville St", "city": "Raleigh", "state": "NC", "zip_code": "27601", "latitude": 35.7796, "longitude": -78.6382, "price": 1250, "bedrooms": 1, "bathrooms": 1, "sqft": 680, "property_type": "apartment", "amenities": ["gym", "pool", "wifi"], "images": []},
    ]

    for data in sample_listings:
        db.add(Listing(**data))
    db.commit()
    db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    seed_database()
    yield


app = FastAPI(
    title="Affordable Housing Finder API",
    description="API for finding affordable housing for new graduates",
    version="1.0.0",
    lifespan=lifespan,
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
