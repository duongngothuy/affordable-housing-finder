"""Seed the database with sample housing listings"""
from app.database import SessionLocal, engine
from app.models import Base, Listing

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    existing = db.query(Listing).first()
    if existing:
        print("Database already has data. Skipping seed.")
        db.close()
        return

    listings = [
        Listing(
            title="Modern Studio in Downtown",
            description="Bright studio apartment with city views, perfect for young professionals",
            address="123 Main St",
            city="San Diego",
            state="CA",
            zip_code="92101",
            latitude=32.7157,
            longitude=-117.1611,
            price=1450,
            bedrooms=0,
            bathrooms=1,
            sqft=450,
            property_type="apartment",
            amenities=["gym", "pool", "parking", "laundry"],
            images=[]
        ),
        Listing(
            title="Cozy 1BR near UCSD",
            description="Walking distance to campus, utilities included",
            address="456 La Jolla Village Dr",
            city="San Diego",
            state="CA",
            zip_code="92093",
            latitude=32.8801,
            longitude=-117.2340,
            price=1800,
            bedrooms=1,
            bathrooms=1,
            sqft=650,
            property_type="apartment",
            amenities=["parking", "laundry", "AC"],
            images=[]
        ),
        Listing(
            title="Affordable Room in Shared House",
            description="Private room in a 4BR house, shared common areas",
            address="789 College Ave",
            city="San Diego",
            state="CA",
            zip_code="92115",
            latitude=32.7633,
            longitude=-117.0701,
            price=850,
            bedrooms=1,
            bathrooms=1,
            sqft=200,
            property_type="room",
            amenities=["wifi", "parking", "backyard"],
            images=[]
        ),
        Listing(
            title="Spacious 2BR Apartment",
            description="Recently renovated with modern appliances",
            address="321 Harbor Dr",
            city="San Diego",
            state="CA",
            zip_code="92101",
            latitude=32.7096,
            longitude=-117.1637,
            price=2400,
            bedrooms=2,
            bathrooms=2,
            sqft=1000,
            property_type="apartment",
            amenities=["gym", "rooftop", "concierge", "parking"],
            images=[]
        ),
        Listing(
            title="Budget-Friendly Studio",
            description="Great starter apartment for recent grads",
            address="555 El Cajon Blvd",
            city="San Diego",
            state="CA",
            zip_code="92115",
            latitude=32.7543,
            longitude=-117.0854,
            price=1200,
            bedrooms=0,
            bathrooms=1,
            sqft=400,
            property_type="apartment",
            amenities=["laundry", "parking"],
            images=[]
        ),
        Listing(
            title="Tech Hub Loft",
            description="Industrial-style loft in the heart of downtown Austin",
            address="100 Congress Ave",
            city="Austin",
            state="TX",
            zip_code="78701",
            latitude=30.2672,
            longitude=-97.7431,
            price=1650,
            bedrooms=1,
            bathrooms=1,
            sqft=750,
            property_type="loft",
            amenities=["gym", "rooftop", "coworking"],
            images=[]
        ),
        Listing(
            title="Affordable Austin Studio",
            description="Perfect for UT grads starting their career",
            address="2500 Guadalupe St",
            city="Austin",
            state="TX",
            zip_code="78705",
            latitude=30.2914,
            longitude=-97.7414,
            price=1100,
            bedrooms=0,
            bathrooms=1,
            sqft=380,
            property_type="apartment",
            amenities=["pool", "laundry"],
            images=[]
        ),
        Listing(
            title="Seattle Starter Home",
            description="Cozy apartment near Amazon HQ",
            address="400 Pine St",
            city="Seattle",
            state="WA",
            zip_code="98101",
            latitude=47.6062,
            longitude=-122.3321,
            price=1900,
            bedrooms=1,
            bathrooms=1,
            sqft=600,
            property_type="apartment",
            amenities=["gym", "concierge", "parking"],
            images=[]
        ),
        Listing(
            title="Denver Mountain View",
            description="Beautiful views of the Rockies",
            address="1600 California St",
            city="Denver",
            state="CO",
            zip_code="80202",
            latitude=39.7392,
            longitude=-104.9903,
            price=1550,
            bedrooms=1,
            bathrooms=1,
            sqft=700,
            property_type="apartment",
            amenities=["gym", "rooftop", "bike storage"],
            images=[]
        ),
        Listing(
            title="Phoenix Budget Living",
            description="Affordable desert living with pool access",
            address="3300 N Central Ave",
            city="Phoenix",
            state="AZ",
            zip_code="85012",
            latitude=33.4484,
            longitude=-112.0740,
            price=950,
            bedrooms=1,
            bathrooms=1,
            sqft=550,
            property_type="apartment",
            amenities=["pool", "gym", "parking"],
            images=[]
        ),
        Listing(
            title="Atlanta Entry-Level Apartment",
            description="Close to tech companies and public transit",
            address="200 Peachtree St",
            city="Atlanta",
            state="GA",
            zip_code="30303",
            latitude=33.7490,
            longitude=-84.3880,
            price=1350,
            bedrooms=1,
            bathrooms=1,
            sqft=620,
            property_type="apartment",
            amenities=["gym", "pool", "parking"],
            images=[]
        ),
        Listing(
            title="Raleigh New Grad Special",
            description="Near Research Triangle Park tech hub",
            address="500 Fayetteville St",
            city="Raleigh",
            state="NC",
            zip_code="27601",
            latitude=35.7796,
            longitude=-78.6382,
            price=1250,
            bedrooms=1,
            bathrooms=1,
            sqft=680,
            property_type="apartment",
            amenities=["gym", "pool", "parking", "wifi"],
            images=[]
        ),
    ]

    for listing in listings:
        db.add(listing)

    db.commit()
    print(f"Successfully seeded {len(listings)} listings!")
    db.close()

if __name__ == "__main__":
    seed_database()
