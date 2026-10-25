"""Schemas de los endpoints de generacion de senales (Milestone 1)."""

from pydantic import BaseModel, Field


class PinkNoiseRequest(BaseModel):
    """Pedido para generar ruido rosa."""

    duration: float = Field(gt=0, le=60)
    sample_rate: int = Field(default=44100, ge=8000, le=192000)
