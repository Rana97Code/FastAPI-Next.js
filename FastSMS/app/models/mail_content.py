from app.config import engine, Base, SessionLocal
from sqlalchemy import Column,String,Integer,Boolean
from pydantic import BaseModel

class MailContent(Base):
    __tablename__="mail_contents"
    id=Column(Integer,primary_key=True,index=True)
    mail_type = Column(String(100),index=True)
    mail_content = Column(String(255),index=True)
    
# for auto datatable create
Base.metadata.create_all(bind=engine)

class McontentCreateSchema(BaseModel):
    # id:int
    mail_type:str
    mail_content:str
   
    class Config:
        orm_mode=True

class MailContentSchema(BaseModel):
    id:int
    mail_type:str
    mail_content:str
   
    class Config:
        orm_mode=True