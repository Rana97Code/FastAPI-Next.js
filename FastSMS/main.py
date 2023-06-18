from sqlalchemy import Column,String,Integer,Boolean
from fastapi import FastAPI,Query,Depends
from fastapi.middleware.cors import CORSMiddleware
from app.config import engine, Base, SessionLocal

#import routers
from app.routers.user_route import user_router
from app.routers.customer_route import customer_router
from app.routers.servicetime_route import servicetime_router
from app.routers.unit_route import unit_router
from app.routers.product_route import product_router
from app.routers.purchase_product_route import p_product_router
from app.routers.mail_content_route import mail_content_router

Base.metadata.create_all(bind=engine)

#include all routers
def include_router(app):
    app.include_router(user_router)
    app.include_router(customer_router)
    app.include_router(servicetime_router)
    app.include_router(unit_router)
    app.include_router(product_router)
    app.include_router(p_product_router)
    app.include_router(mail_content_router)

#for connect with next.js
origins = [
    "http://localhost:3000",
]

def start_application():
    app=FastAPI()
    include_router(app)


    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
    return app



app = start_application()

