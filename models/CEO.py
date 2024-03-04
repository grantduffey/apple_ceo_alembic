from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
import Base.py

class CEO(Base):
    __tablename__ = "apple_ceos_alembic"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)
    year = Column(Integer)
    
class CEOSchema(BaseModel):
    name: str
    slug: str
    year: int
    
    class Config:
        populate_by_name = True