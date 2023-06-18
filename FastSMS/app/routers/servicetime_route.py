from fastapi import APIRouter,Depends,HTTPException
from typing import Union,List,Optional
from sqlalchemy.orm import Session
from app.models.service_time import ServiceTimeCreateSchema,ServiceTimeSchema,Service_time
from app.config import engine, Base, SessionLocal, get_db
from fastapi.responses import JSONResponse



servicetime_router = APIRouter()

@servicetime_router.post("/servicetime_add")
def create(service:ServiceTimeCreateSchema,db:Session=Depends(get_db)):
    srv=Service_time(year=service.year,month=service.month,service_details=service.service_details)
    db.add(srv)
    db.commit()
    return {"Message":"Successfully Add"}

@servicetime_router.get("/servicetime",response_model=List[ServiceTimeSchema])
def index(db:Session=Depends(get_db)):
    return db.query(Service_time).all()


@servicetime_router.get("/get_servicetime/{st_id}",response_model=ServiceTimeSchema)
def get_itm(st_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Service_time).filter(Service_time.id == st_id).first()
        return (u)
    except:
        return HTTPException(status_code=422, details="Unit not found")
    

@servicetime_router.put("/update_servicetime/{st_id}")
def update(st_id:int,service:ServiceTimeCreateSchema,db:Session=Depends(get_db)):
    try:
        u=db.query(Service_time).filter(Service_time.id==st_id).first()
        u.year=service.year,
        u.month=service.month,
        u.service_details=service.service_details
        db.add(u)
        db.commit()
        return {"Message":"Successfully Update"}
    except:
        return HTTPException(status_code=404,detail="Update Uncessfull")


@servicetime_router.delete("/delete_stime/{st_id}",response_class=JSONResponse)
def delete(st_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Service_time).filter(Service_time.id==st_id).first()
        db.delete(u)
        db.commit()
        return {"Service Time has been deleted"}
    except:
        return HTTPException(status_code=422, details="user not found")