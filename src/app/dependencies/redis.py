from app.database import get_redis_client

def get_redis():
    return get_redis_client()