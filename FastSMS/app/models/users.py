from app.config import engine, Base, SessionLocal
from sqlalchemy import Column,String,Integer,Boolean
from pydantic import BaseModel
import passlib.hash as _hash


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    user_name = Column(String(255),unique=True,index=True)
    user_phone = Column(String(255),unique=True,index=True)
    user_email = Column(String(255),unique=True,index=True)
    user_password = Column(String(255),unique=True,index=True)
    confirm_password = Column(String(255),unique=True,index=True)
    
    #for passwod verification
    def verify_password(self, user_password: str):
        return _hash.bcrypt.verify(user_password, self.user_password)

Base.metadata.create_all(bind=engine)

class UserCreateSchema(BaseModel):
    user_name:str
    user_phone:str
    user_email:str
    user_password:str
    class Config:
        orm_mode=True

class UserSchema(BaseModel):
    id:int
    user_name:str
    user_phone:str
    user_email:str
    user_password:str
    class Config:
        orm_mode=True

class TokenData(BaseModel):
    user_email: str | None = None

        
class UserInDB(BaseModel):
    user_password: str
    class Config:
        orm_mode=True


class SigninRequest(BaseModel):
    user_email:str
    user_password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenJson(BaseModel):
    access_token: str
    token_type: str

class UserRead(BaseModel):
    user_email: str
   