from fastapi import APIRouter,Depends,HTTPException
from typing import Union,List,Optional
from sqlalchemy.orm import Session
from app.models.customers import CustomerCreateSchema,CustomerSchema,Customer
from app.config import engine, Base, SessionLocal, get_db
from fastapi.responses import JSONResponse

customer_router = APIRouter()


@customer_router.post("/customer_add")
def create(customer:CustomerCreateSchema,db:Session=Depends(get_db)):
    srv=Customer(customer_name=customer.customer_name,customer_email=customer.customer_email,customer_phone=customer.customer_phone,customer_address=customer.customer_address)
    db.add(srv)
    db.commit()
    return {"Message":"Successfully Add"}

@customer_router.get("/customers",response_model=List[CustomerSchema])
def index(db:Session=Depends(get_db)):
    return db.query(Customer).all()


@customer_router.get("/get_customer/{st_id}",response_model=CustomerSchema)
def get_itm(st_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Customer).filter(Customer.id == st_id).first()
        return (u)
    except:
        return HTTPException(status_code=422, details="Unit not found")
    

@customer_router.put("/update_customer/{st_id}")
def update(st_id:int,customer:CustomerCreateSchema,db:Session=Depends(get_db)):
    try:
        u=db.query(Customer).filter(Customer.id==st_id).first()
        u.customer_name=customer.customer_name,
        u.customer_email=customer.customer_email,
        u.customer_phone=customer.customer_phone,
        u.customer_address=customer.customer_address
        db.add(u)
        db.commit()
        return {"Message":"Successfully Update"}
    except:
        return HTTPException(status_code=404,detail="Update Uncessfull")


@customer_router.delete("/delete_customer/{st_id}",response_class=JSONResponse)
def delete(st_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Customer).filter(Customer.id==st_id).first()
        db.delete(u)
        db.commit()
        return {"Customer has been deleted"}
    except:
        return HTTPException(status_code=422, details="user not found")