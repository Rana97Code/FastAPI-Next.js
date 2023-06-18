from fastapi import APIRouter,Depends,HTTPException, Response
from typing import Union,List,Optional
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models.products import ProductCreateSchema,ProductSchema,Product
from app.models.units import Unit,UnitSchema
from app.models.purchase_product import Purchase_product
from app.config import get_db
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder





product_router = APIRouter()


@product_router.post("/product_add")
def create(product:ProductCreateSchema,db:Session=Depends(get_db)):
    srv=Product(unit_id=product.unit_id,product_name=product.product_name,product_sku=product.product_sku,product_qty=product.product_qty,product_details=product.product_details)
    db.add(srv)
    db.commit()
    return {"Message":"Successfully Add"}

@product_router.get("/products")
def index(db:Session=Depends(get_db)):
    unit = db.query(Product,Unit).join(Unit, Product.unit_id == Unit.id ).add_columns(Unit.unit_name, Product.product_name,Product.product_qty, Product.product_details).all()
    # unit = db.query(Product, Unt).join(Unt, Unt.id==Product.unit_id).all()
    untt = []
    for unt in unit:
        # print(unt.unit_name, unt.product_name)
        untt.append({
            'unit_name':unt.unit_name,
            'product_name':unt.product_name,
            'product_qty':unt.product_qty,
            'product_details':unt.product_details
            })

    junit = jsonable_encoder(untt)
    return JSONResponse(content=junit)




@product_router.get("/get_product/{st_id}",response_model=ProductSchema)
def get_itm(st_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Product).filter(Product.id == st_id).first()
        return (u)
    except:
        return HTTPException(status_code=422, details="Unit not found")
    

@product_router.put("/update_Product/{st_id}")
def update(st_id:int,product:ProductCreateSchema,db:Session=Depends(get_db)):
    try:
        u=db.query(Product).filter(Product.id==st_id).first()
        u.unit_id=product.unit_id,
        u.product_name=product.product_name,
        u.product_sku=product.product_sku,
        u.product_qty=product.product_qty,
        u.product_details=product.product_details
        db.add(u)
        db.commit()
        return {"Message":"Successfully Update"}
    except:
        return HTTPException(status_code=404,detail="Update Uncessfull")


@product_router.delete("/delete_product/{st_id}",response_class=JSONResponse)
def delete(st_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Product).filter(Product.id==st_id).first()
        db.delete(u)
        db.commit()
        return {"Product has been deleted"}
    except:
        return HTTPException(status_code=422, details="user not found")