from fastapi import FastAPI
from routes import base
app = FastAPI()



# we tell app we have route in base use iy 
app.include_router(base.base_router)
