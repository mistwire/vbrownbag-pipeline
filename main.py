from fastapi import FastAPI
from app.api.routes import router
from dotenv import load_dotenv

# Load env variables from .env
# This must happen before anything tries to read them

load_dotenv()

app = FastAPI()

# Register the router — plug the subnet into the main network
app.include_router(router)
