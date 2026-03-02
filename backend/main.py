from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .app.api import api as api_router

app = FastAPI(title="PMQ Backend Skeleton")
app.include_router(api_router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "0.1.0"}
