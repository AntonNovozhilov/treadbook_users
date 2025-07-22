from fastapi import FastAPI
from app.api.api_v1.main_router import main_router

app = FastAPI()
app.include_router(main_router)



