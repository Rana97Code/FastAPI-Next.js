from app.config import engine, Base, SessionLocal
from sqlalchemy import Column,String,Integer,Boolean,Date,DateTime
from pydantic import BaseModel
# from typing import Annotated #
# from fastapi import Body
from datetime import datetime, time

class Purchase_product(Base):
    __tablename__="purchase_products"
    id=Column(Integer,primary_key=True,index=True)
    product_id=Column(Integer,index=True)
    customer_id=Column(Integer,index=True)
    p_qty=Column(Integer,index=True)
    purchase_date = Column(DateTime,index=True, default=datetime.utcnow())
    expiry_date = Column(DateTime,index=True, default=datetime.utcnow())
    renew_date = Column(DateTime,index=True, default=datetime.utcnow())    
    service_time = Column(String(255),unique=True,index=True)    

Base.metadata.create_all(bind=engine)

class PurchaseProCreateSchema(BaseModel):
    product_id:int
    customer_id:int
    purchase_date:str
    expiry_date:str
    renew_date:str
    service_time:str
    class Config:
        orm_mode=True

class PurchaseProductSchema(BaseModel):
    id:int 
    product_id:int 
    customer_id:int 
    purchase_date:datetime | None
    expiry_date:datetime | None 
    renew_date:datetime | None
    service_time:str 
    class Config:
        orm_mode=True
