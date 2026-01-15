from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from app.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False, index=True)
    state = Column(String, nullable=False, index=True)
    zip_code = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    price = Column(Integer, nullable=False, index=True)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Float, nullable=False)
    sqft = Column(Integer)
    property_type = Column(String, nullable=False)
    amenities = Column(JSON, default=[])
    images = Column(JSON, default=[])
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
