from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DevOps Platform API is running"}
