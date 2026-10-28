from fastapi import FastAPI
# we put it before import base because we want to load env before any thing else

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")  # Load environment variables from .env file

from src.routes import base 
app = FastAPI()



# we tell app we have route in base use iy 
app.include_router(base.base_router)
