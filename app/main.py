from fastapi import FastAPI

from app.api.routers import anonymize_text


app = FastAPI()
app.include_router(anonymize_text.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Haru's Creek AI!"}
