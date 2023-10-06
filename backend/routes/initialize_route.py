from typing import Annotated
from fastapi import APIRouter, Form
from service.InitializeSevice import InitializeSevice

router = APIRouter(
    prefix='/api',
    tags=['initialize']
)

@router.get('/initialize')
async def initialize():
    initializeSevice = InitializeSevice()
    return {
        "message": initializeSevice.initialize()
    }

@router.get('/reset')
async def reset():
    initializeSevice = InitializeSevice()
    return {
        "message": initializeSevice.reset()
    }