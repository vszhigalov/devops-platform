from fastapi import FastAPI
import os
import psycopg2
import redis

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")


@app.get("/")
def root():
    return {
        "message": "DevOps Platform API is running",
        "database_url": DATABASE_URL,
        "redis_url": REDIS_URL,
    }


@app.get("/health")
def health():
    postgres_status = "disconnected"
    redis_status = "disconnected"

    try:
        conn = psycopg2.connect(DATABASE_URL)
        postgres_status = "connected"
        conn.close()
    except Exception:
        pass

    try:
        r = redis.from_url(REDIS_URL)
        r.ping()
        redis_status = "connected"
    except Exception:
        pass

    return {
        "api": "healthy",
        "postgres": postgres_status,
        "redis": redis_status,
    }
