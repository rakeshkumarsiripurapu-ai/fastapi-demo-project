from fastapi import FastAPI
from app.api import router

app = FastAPI(title="FastAPI Demo Project")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "FastAPI Demo Project is running"}
