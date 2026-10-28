
from fastapi import FastAPI ,APIRouter

base_router = APIRouter()



@base_router.get("/")
def welcome():
    return {"message": "Welcome to FastAPI! this is splited router from main file"}
