
from fastapi import  APIRouter 

import os

base_router = APIRouter(
    #any routes down you should put prefix befor routes name becaue in future if clint ask to add or put name four routes you can easily add prefix to all routes in this router
prefix="/api/v1",
#split tags  on swageer
tags=["Api/v1"]
)



@base_router.get("/")
async def welcome():
    app_name=os.getenv("APP_NAME")
    app_version=os.getenv("APP_VERSION")
    return {"message": "Welcome to FastAPI! this is splited router from main file", "app_name": app_name, "app_version": app_version}
