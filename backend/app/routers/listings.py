from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models import Listing
from app.schemas import ListingResponse

router = APIRouter()

@router.get("/", response_model=List[ListingResponse])
async def get_listings(
    city: Optional[str] = Query(None),
    state: Optional[str] = Query(None),
    min_price: Optional[int] = Query(None, ge=0),
    max_price: Optional[int] = Query(None, ge=0),
    bedrooms: Optional[int] = Query(None, ge=0),
    property_type: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(Listing)
    if city:
        query = query.filter(Listing.city.ilike(f"%{city}%"))
    if state:
        query = query.filter(Listing.state.ilike(state))
    if min_price is not None:
        query = query.filter(Listing.price >= min_price)
    if max_price is not None:
        query = query.filter(Listing.price <= max_price)
    if bedrooms is not None:
        query = query.filter(Listing.bedrooms == bedrooms)
    if property_type:
        query = query.filter(Listing.property_type.ilike(property_type))
    return query.all()

@router.get("/{listing_id}", response_model=ListingResponse)
async def get_listing(listing_id: int, db: Session = Depends(get_db)):
    listing = db.query(Listing).filter(Listing.id == listing_id).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing
