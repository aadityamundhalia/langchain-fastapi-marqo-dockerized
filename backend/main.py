from fastapi import FastAPI
from routes import upload_router, index_router, chat_router, initialize_route
from routes import image_route

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Application ready"}

# upload router
app.include_router(upload_router.router)
# index router
app.include_router(index_router.router)
# chat router
app.include_router(chat_router.router)
# initialize router
app.include_router(initialize_route.router)
# image router
app.include_router(image_route.router)
