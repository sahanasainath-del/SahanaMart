from app.database import SessionLocal
from app.models import User, Seller

db = SessionLocal()

user = db.query(User).filter(
    User.email == "admin@sahanamart.com"
).first()

if not user:
    print("Admin user not found.")
else:
    seller = db.query(Seller).filter(
        Seller.user_id == user.id
    ).first()

    if seller:
        print("Seller already exists.")
    else:
        seller = Seller(
            user_id=user.id,
            business_name="SahanaMart Store"
        )

        db.add(seller)
        db.commit()
        db.refresh(seller)

        print("Seller created successfully!")
        print("Seller ID:", seller.id)

db.close()