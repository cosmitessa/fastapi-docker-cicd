from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    version: str
    timestamp: datetime

class EchoRequest(BaseModel):
    """Request model for echo endpoint"""
    message: str = Field(..., min_length=1, max_length=500, description="Message to echo")
    metadata: Optional[dict] = Field(default=None, description="Optional metadata")

class EchoResponse(BaseModel):
    """Response model for echo endpoint"""
    original_message: str
    echoed_at: datetime
    metadata: Optional[dict] = None