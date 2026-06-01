from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Using SQLite for rapid development and testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# check_same_thread is required for SQLite in FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# This creates a database session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All of our database models will inherit from this Base class
Base = declarative_base()

# Dependency to get the database session in our API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()