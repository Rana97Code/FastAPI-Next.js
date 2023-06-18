from app.config import engine, Base, SessionLocal
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
# from app.models.units import UnitSchema
# from app.models.units import Unit



class Product(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True,index=True)
    unit_id = Column(Integer, ForeignKey("units.id"))
    product_name = Column(String(255),index=True)
    product_sku = Column(String(255),unique=True,index=True)
    product_qty = Column(Integer,index=True)
    product_details = Column(String(255),index=True)

    # un = relationship("Unt", backref="products",  foreign_keys=[unit_id])


# class Unt(Base):
#     __tablename__="units"
#     id=Column(Integer,primary_key=True,index=True)
#     unit_name = Column(String(255),unique=True,index=True)
#     unit_details = Column(String(255),unique=True,index=True)

    # prod = relationship("Product", backref="un")


Base.metadata.create_all(bind=engine)

class ProductCreateSchema(BaseModel):
    # id:int
    unit_id:int
    product_name:str
    product_sku:str
    product_qty:int
    product_details:str

    class Config:
        orm_mode=True

class UnitBase(BaseModel):
    unit_name:str
    unit_details:str

    class Config:
        orm_mode=True

class ProductSchema(BaseModel):
    id:int
    unit_id:int
    product_name:str
    product_sku:str
    product_qty:int
    product_details:str

    class Config:
        orm_mode=True


# class ProductUnitSchema(BaseModel):
#     unit_name:str
#     product_name:str
#     unit_details:str

#     class Config:
#         orm_mode=True