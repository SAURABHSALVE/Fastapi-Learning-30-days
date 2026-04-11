# Your database tables.
## code for SQLAlchemy models (e.g., User model).
from sqlalchemy import Column, Integer, String, Boolean, Index
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key = True,index =True)
    
    email = Column(String,unique = True,index = True)

    hashed_password = Column(String(255), nullable=False)
    
    is_active = Column(Boolean,default = True )
    
    def __repr__(self):
        return f"<User(email='{self.email}', is_active={self.is_active})>"
        