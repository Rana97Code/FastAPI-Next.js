from fastapi import APIRouter, Depends, HTTPException
from typing import Union,List,Optional
from sqlalchemy.orm import Session
from app.models.purchase_product import PurchaseProCreateSchema,PurchaseProductSchema,Purchase_product
from app.models.products import Product
from app.models.customers import Customer
from app.models.units import Unit
from app.config import engine, Base, SessionLocal, get_db
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

p_product_router = APIRouter()

@p_product_router.post("/add_purchase_product")
def create(p_p:PurchaseProCreateSchema,db:Session=Depends(get_db)):
    srv=Purchase_product(product_id=p_p.product_id,customer_id=p_p.customer_id,purchase_date=p_p.purchase_date,expiry_date=p_p.expiry_date,renew_date=p_p.renew_date,service_time=p_p.service_time)
    db.add(srv)
    db.commit()
    return {"Message":"Successfully Add"}

@p_product_router.get("/purchase_products",response_model=List[PurchaseProductSchema])
def index(db:Session=Depends(get_db)):
    p_p = db.query(Purchase_product,Product,Customer,Unit).join(Product, Purchase_product.product_id == Product.id ).join(Customer, Purchase_product.customer_id == Customer.id )\
    .join(Unit, Product.unit_id == Unit.id )\
    .add_columns( Product.product_name,Customer.customer_name,Purchase_product.p_qty,Unit.unit_name, Purchase_product.purchase_date, Purchase_product.expiry_date,Purchase_product.service_time).all()
    p_pro = []
    for pp in p_p:
        # print(pp.product_name, pp.customer_name,pp.unit_name)
        p_pro.append({
            'product_name':pp.product_name,
            'customer_name':pp.customer_name,
            'p_qty':pp.p_qty,
            'unit_name':pp.unit_name,
            'purchase_date':pp.purchase_date,
            'expiry_date':pp.expiry_date,
            'service_time':pp.service_time
            })

    junit = jsonable_encoder(p_pro)
    return JSONResponse(content=junit)
    # return db.query(Purchase_product).all()

@p_product_router.get("/get_purchase_product/{pp_id}",response_model=PurchaseProductSchema)
def get_itm(pp_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Purchase_product).filter(Purchase_product.id == pp_id).first()
        return (u)
    except:
        return HTTPException(status_code=422, details="Purchase Product not found")

@p_product_router.put("/update_purchase_product/{pp_id}")
def update(pp_id:int,p_product:PurchaseProCreateSchema,db:Session=Depends(get_db)):
    try:
        u=db.query(Purchase_product).filter(Purchase_product.id==pp_id).first()
        u.product_id=p_product.product_id,
        u.customer_id=p_product.customer_id,
        u.purchase_date=p_product.purchase_date,
        u.expiry_date=p_product.expiry_date,
        u.renew_date=p_product.renew_date,
        u.service_time=p_product.service_time
        db.add(u)
        db.commit()
        return {"Message":"Successfully Update"}
    except:
        return HTTPException(status_code=404,detail="Update Uncessfull")

@p_product_router.delete("/delete_Purchase_product/{pp_id}",response_class=JSONResponse)
def get_itm(pp_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Purchase_product).filter(Purchase_product.id==pp_id).first()
        db.delete(u)
        db.commit()
        return {"Purchase_product has been deleted"}
    except:
        return HTTPException(status_code=422, details="user not found")