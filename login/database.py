from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Database Location
# sql_app.db will be created in your root directory
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# 2. Engine Configuration
# 'check_same_thread': False is mandatory for SQLite in FastAPI 
# to allow multiple threads to access the database safely.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# 3. Session Factory
# This creates a "SessionLocal" class. Each instance of this 
# will be an actual database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base Class for Models
# Your SQLAlchemy models (User, Profile, etc.) will inherit from this Base.
Base = declarative_base()

# 5. Dependency (The "get_db" function)
# This is used in FastAPI routes via Depends(get_db).
# It ensures every request gets its own session and closes it afterward.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()