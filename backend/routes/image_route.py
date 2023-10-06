from typing import Annotated
from fastapi import APIRouter, Form
from service.UploadService import UploadService

router = APIRouter(
    prefix='/api',
    tags=['image']
)


@router.post('/image')
async def image(image: Annotated[str, Form()]):
    uploadService = UploadService(image, image=True)

    return {
        "message": uploadService.embedFile(),
    }
