import time

from fastapi import APIRouter

from app.db.connections import check_postgres, check_redis

router = APIRouter()


@router.get("/health")
def health():
    return {
        "api": "healthy",
        "postgres": check_postgres(),
        "redis": check_redis(),
    }


@router.get("/slow")
def slow():
    time.sleep(1)

    return {"status": "slow endpoint"}
