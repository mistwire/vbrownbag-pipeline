from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

# Register the router — plug the subnet into the main network
app.include_router(router)
