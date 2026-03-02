from fastapi import APIRouter

api = APIRouter()


@api.get("/health")
def health():
    return {"status": "ok"}
