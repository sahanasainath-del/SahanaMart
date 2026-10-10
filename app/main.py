from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .database import engine, Base
from . import models
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SahanaMart API")

app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
return FileResponse("static/login.html")
