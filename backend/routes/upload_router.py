from fastapi import APIRouter
from fastapi import UploadFile
from service.UploadService import UploadService

router = APIRouter(
    prefix='/api',
    tags=['upload']
)


@router.post('/upload')
async def store(file: UploadFile):
    uploadService = UploadService(file)

    return {
        "message": uploadService.embedFile(),
    }
