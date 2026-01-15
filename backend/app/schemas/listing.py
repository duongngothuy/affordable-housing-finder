from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ListingBase(BaseModel):
    title: str
    description: Optional[str] = None
    address: str
    city: str
    state: str
    zip_code: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    price: int
    bedrooms: int
    bathrooms: float
    sqft: Optional[int] = None
    property_type: str
    amenities: List[str] = []
    images: List[str] = []

class ListingCreate(ListingBase):
    pass

class ListingResponse(ListingBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
