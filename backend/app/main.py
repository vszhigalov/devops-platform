from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.routes.health import router as health_router
from app.api.routes.users import router as users_router

app = FastAPI(title="DevOps Platform API")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")
Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {"message": "DevOps Platform API is running"}


@app.get("/2048", response_class=HTMLResponse)
def game(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request},
    )


app.include_router(health_router)
app.include_router(users_router)
