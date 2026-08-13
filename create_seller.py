from app.database import SessionLocal
from app.models import User, Seller
from app.auth import hash_password

db = SessionLocal()

seller_email = "seller@sahanamart.com"

existing_user = db.query(User).filter(
    User.email == seller_email
).first()

if existing_user:
    print("Seller user already exists.")
    print("Email:", existing_user.email)
    print("Role:", existing_user.role)

else:
    seller_user = User(
        name="Sahana Seller",
        email=seller_email,
        password=hash_password("Seller@123"),
        role="SELLER"
    )

    db.add(seller_user)
    db.commit()
    db.refresh(seller_user)

    seller = Seller(
        user_id=seller_user.id,
        business_name="SahanaMart Store"
    )

    db.add(seller)
    db.commit()
    db.refresh(seller)

    print("Seller created successfully!")
    print("Email:", seller_email)
    print("Password: Seller@123")
    print("Seller ID:", seller.id)

db.close()