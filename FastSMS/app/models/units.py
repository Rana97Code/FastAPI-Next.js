from app.config import engine, Base, SessionLocal
from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from app.models.products import Product


class Unit(Base):
    __tablename__="units"
    id=Column(Integer,primary_key=True,index=True)
    unit_name = Column(String(255),unique=True,index=True)
    unit_details = Column(String(255),unique=True,index=True)
    # product = relationship("Product", backref="unit")
    # prod = relationship(Product)


Base.metadata.create_all(bind=engine)

class UnitCreateSchema(BaseModel):
    unit_name:str
    unit_details:str
    class Config:
        orm_mode=True

class UnitSchema(BaseModel):
    id:int
    unit_name:str
    unit_details:str
    class Config:
        orm_mode=True

class UnitBase(BaseModel):
    unit_name:str
    unit_details:str

    class Config:
        orm_mode=True