from typing import Annotated
from fastapi import APIRouter, Form
from service.ChatService import ChatService

router = APIRouter(
    prefix='/api',
    tags=['chat']
)


@router.post('/chat/{index}')
async def getDocuments(index, query: Annotated[str, Form()]):
    chatService = ChatService(index)
    return {
        "message": chatService.chat(query)
    }


@router.post('/tool-box')
async def getToolBox(query: Annotated[str, Form()]):
    chatService = ChatService()
    return {
        "message": chatService.toolBox(query)
    }


@router.post('/duckduckgo')
async def getDuckduckgo(query: Annotated[str, Form()]):
    chatService = ChatService()
    return {
        "message": chatService.duckduckgo(query)
    }
