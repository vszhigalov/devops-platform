from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.users import router as users_router

app = FastAPI(title="DevOps Platform API")


@app.get("/")
def root():
    return {"message": "DevOps Platform API is running"}


app.include_router(health_router)
app.include_router(users_router)
