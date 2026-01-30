from fastapi import APIRouter, Depends, status

from redis.asyncio import Redis

from app.schemas import DocumentSend, DocumentResponce
from app.services import verify
from app.dependencies import get_redis

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
    responses={422:{"description": "Invalid data"}}
)


@router.post(
    "/",
    response_model= DocumentResponce,
    status_code=status.HTTP_201_CREATED,
    summary="Отправить документ на проверку",
    description="Отправляет документ на проверку и возвращает результат проверки",
)
async def check_document(document: DocumentSend,
                    redis: Redis = Depends(get_redis)
                    ) -> DocumentResponce:
    check = await redis.get(hash(document))
    if not check:
        check = verify(
            document.date_of_birth,
            document.doc_number,
            document.mrz
            )
        await redis.set(hash(document), check)
    return DocumentResponce(result=check)