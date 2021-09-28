from fastapi import FastAPI
from . import models
from .database import engine
from .routers import inventory, users, login

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(login.router)
app.include_router(inventory.router)
app.include_router(users.router)
