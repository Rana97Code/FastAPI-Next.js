from app.config import engine, Base, SessionLocal
from sqlalchemy import Column,String,Integer,Boolean
from pydantic import BaseModel

class Service_time(Base):
    __tablename__="service_time"
    id=Column(Integer,primary_key=True,index=True)
    year = Column(Integer)
    month = Column(Integer)
    service_details = Column(String(255))

Base.metadata.create_all(bind=engine)

class ServiceTimeCreateSchema(BaseModel):
    # id:int
    year:int
    month:int
    service_details:str
    class Config:
        orm_mode=True

class ServiceTimeSchema(BaseModel):
    id:int
    year:int
    month:int
    service_details:str
    class Config:
        orm_mode=True
