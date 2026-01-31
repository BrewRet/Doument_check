from fastapi import APIRouter

from app.schemas import HealthResponse

router = APIRouter(
    prefix="/healthz",
    tags=["healthz"],
)

@router.get("", response_model=HealthResponse)
def healthz_check():
    """Проверка работоспособности сервиса."""

    return HealthResponse(status="ok")