from fastapi import APIRouter, Depends, HTTPException
from typing import Union,List,Optional
from sqlalchemy.orm import Session
from app.models.units import UnitCreateSchema,UnitSchema,Unit #there two schema one are create and another one is get data id_wise
from app.config import get_db
from fastapi.responses import JSONResponse

#route define
unit_router = APIRouter()

@unit_router.post("/add_unit")
def create(unit:UnitCreateSchema,db:Session=Depends(get_db)): #data field define using schema and session manage
    srv=Unit(unit_name=unit.unit_name,unit_details=unit.unit_details)
    db.add(srv)
    db.commit()
    return {"Message":"Successfully Add"}

@unit_router.get("/units",response_model=List[UnitSchema])
def index(db:Session=Depends(get_db)):
    return db.query(Unit).all()

@unit_router.get("/get_unit/{unit_id}",response_model=UnitSchema)
def get_itm(unit_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Unit).filter(Unit.id == unit_id).first()
        return (u)
    except:
        return HTTPException(status_code=422, details="Unit not found")

@unit_router.put("/update_unit/{unit_id}")
def update(unit_id:int,unit:UnitCreateSchema,db:Session=Depends(get_db)):
    try:
        u=db.query(Unit).filter(Unit.id==unit_id).first()
        u.unit_name=unit.unit_name,
        u.unit_details=unit.unit_details
        db.add(u)
        db.commit()
        return {"Message":"Successfully Update"}
    except:
        return HTTPException(status_code=404,detail="Update Uncessfull")

@unit_router.delete("/delete_unit/{unit_id}",response_class=JSONResponse)
def get_itm(unit_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Unit).filter(Unit.id==unit_id).first()
        db.delete(u)
        db.commit()
        return {"Unit has been deleted"}
    except:
        return HTTPException(status_code=422, details="user not found")