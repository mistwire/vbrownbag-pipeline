from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api.routes import router

# Load env variables from .env
# This must happen before anything tries to read them


app = FastAPI()

# Register the router — plug the subnet into the main network
app.include_router(router)
