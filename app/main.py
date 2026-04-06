from fastapi import FastAPI, HTTPException
from datetime import datetime
import os
import socket
import sys

from models import HealthResponse, EchoRequest, EchoResponse

# Create FastAPI app
app = FastAPI(
    title="Day 3 Container API",
    description="Simple API for learning Docker and CI/CD",
    version="1.0.0"
)

@app.get("/", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        timestamp=datetime.now()
    )


@app.get("/api/info")
async def get_info():
    return {
        "python_version": sys.version,
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development")
    }


@app.post("/api/echo", response_model=EchoResponse)
async def echo_message(request: EchoRequest):
    return EchoResponse(
        original_message=request.message,
        echoed_at=datetime.now(),
        metadata=request.metadata
    )


@app.get("/health")
async def container_health():
    """Docker health check endpoint"""
    return {"status": "ok"}