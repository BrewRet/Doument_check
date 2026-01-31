from unittest.mock import AsyncMock, patch

from tests.conftest import mock_redis
from fastapi import HTTPException
from app.dependencies import get_redis

from app.main import app


async def test_health_returns_ok(async_client):
    response = await async_client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

