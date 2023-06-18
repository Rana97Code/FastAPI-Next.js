from fastapi import APIRouter,Depends,HTTPException
from typing import Union,List,Optional
from sqlalchemy.orm import Session
from app.models.mail_content import McontentCreateSchema,MailContentSchema,MailContent
from app.config import get_db
from fastapi.responses import JSONResponse

mail_content_router = APIRouter()


@mail_content_router.post("/new_content_add")
def create(mailc:McontentCreateSchema,db:Session=Depends(get_db)):
    srv=MailContent(mail_type=mailc.mail_type,mail_content=mailc.mail_content)
    db.add(srv)
    db.commit()
    return {"Message":"Successfully Add"}

@mail_content_router.get("/allmail_content",response_model=List[MailContentSchema])
def index(db:Session=Depends(get_db)):
    return db.query(MailContent).all()


@mail_content_router.get("/get_mail_content/{st_id}",response_model=MailContentSchema)
def get_itm(st_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(MailContent).filter(MailContent.id == st_id).first()
        return (u)
    except:
        return HTTPException(status_code=422, details="Unit not found")
    

@mail_content_router.put("/update_content/{st_id}")
def update(st_id:int,content:McontentCreateSchema,db:Session=Depends(get_db)):
    try:
        u=db.query(MailContent).filter(MailContent.id==st_id).first()
        u.mail_type=content.mail_type,
        u.mail_content=content.mail_content,
      
        db.add(u)
        db.commit()
        return {"Message":"Successfully Update"}
    except:
        return HTTPException(status_code=404,detail="Update Uncessfull")


@mail_content_router.delete("/delete_content/{st_id}",response_class=JSONResponse)
def delete(st_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(MailContent).filter(MailContent.id==st_id).first()
        db.delete(u)
        db.commit()
        return {"Content has been deleted"}
    except:
        return HTTPException(status_code=422, details="user not found")