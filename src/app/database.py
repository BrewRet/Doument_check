import redis.asyncio as redis
from .config import get_settings

settings = get_settings()

redis_client = None

def get_redis_client():
    global redis_client
    if redis_client is None:
        redis_client = redis.Redis(host=settings.redis_host)
    return redis_client