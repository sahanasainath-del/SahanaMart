import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sahanamart.db")

# Render PostgreSQL URLs may use the postgres:// scheme.

# SQLAlchemy expects postgresql://.

if DATABASE_URL.startswith("postgres://"):
DATABASE_URL = DATABASE_URL.replace(
"postgres://", "postgresql://", 1
)

# Configure the engine based on the database type.

if DATABASE_URL.startswith("sqlite"):
engine = create_engine(
DATABASE_URL,
connect_args={"check_same_thread": False}
)
else:
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
autocommit=False,
autoflush=False,
bind=engine
)

Base = declarative_base()

def get_db():
db = SessionLocal()
try:
yield db
finally:
db.close()
