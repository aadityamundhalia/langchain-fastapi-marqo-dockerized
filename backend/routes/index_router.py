from typing import Annotated
from fastapi import APIRouter, Form
from service.IndexService import IndexService

router = APIRouter(
    prefix='/api',
    tags=['index']
)


@router.delete('/index/{index_name}')
async def destroy(index_name):
    indexRepository = IndexService(index_name)
    return {
        "message": indexRepository.deleteIndex()
    }


@router.get('/index')
async def index():
    indexRepository = IndexService()
    return {
        "message": indexRepository.listIndex()
    }


@router.post('/get-documents/{index}')
async def getDocuments(index, query: Annotated[str, Form()]):
    indexRepository = IndexService(index)
    return {
        "message": indexRepository.getDocuments(query)
    }


@router.post('/delete-documents/{index}')
async def deleteDocument(index, query: Annotated[str, Form()]):
    indexRepository = IndexService(index)
    return {
        "message": indexRepository.deleteDocument(query)
    }
