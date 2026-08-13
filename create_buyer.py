from app.database import SessionLocal
from app.models import User
from passlib.context import CryptContext

db = SessionLocal()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

email = "buyer@sahanamart.com"
password = "Buyer@123"

existing_user = db.query(User).filter(
    User.email == email
).first()

if existing_user:
    print("Buyer already exists!")
else:
    buyer = User(
        name="SahanaMart Buyer",
        email=email,
        password=pwd_context.hash(password),
        role="BUYER"
    )

    db.add(buyer)
    db.commit()

    print("Buyer created successfully!")
    print("Email:", email)
    print("Password:", password)
    print("Role: BUYER")

db.close()