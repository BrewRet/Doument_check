import httpx
import pytest
from httpx import ASGITransport
from unittest.mock import Mock

from app.main import app


@pytest.fixture
async def async_client():
    """Асинхронный клиент для тестирования."""


    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="session")
def mock_redis():
    return Mock()