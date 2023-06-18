from app.config import engine, Base, SessionLocal,metadata
from sqlalchemy import Column,String,Integer,Boolean
from pydantic import BaseModel

class Customer(Base):
    __tablename__="customers"
    metadata
    id=Column(Integer,primary_key=True,index=True)
    customer_name = Column(String(255),unique=True,index=True)
    customer_email = Column(String(255),unique=True,index=True)
    customer_phone = Column(String(255),unique=True,index=True)
    customer_address = Column(String(255),unique=True,index=True)

Base.metadata.create_all(bind=engine)

class CustomerCreateSchema(BaseModel):
    # id:int
    customer_name:str
    customer_email:str
    customer_phone:str
    customer_address:str

    class Config:
        orm_mode=True

class CustomerSchema(BaseModel):
    id:int
    customer_name:str
    customer_email:str
    customer_phone:str
    customer_address:str

    class Config:
        orm_mode=True