import psycopg2
import redis

from app.core.config import settings


def check_postgres():
    try:
        conn = psycopg2.connect(settings.DATABASE_URL)
        conn.close()
        return "connected"
    except Exception:
        return "disconnected"


def check_redis():
    try:
        r = redis.from_url(settings.REDIS_URL)
        r.ping()
        return "connected"
    except Exception:
        return "disconnected"
