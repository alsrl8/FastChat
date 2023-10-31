from fastapi import FastAPI

import database
import service

app = FastAPI()

app.include_router(database.router)
app.include_router(service.router)
