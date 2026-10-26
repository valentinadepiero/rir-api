"""Endpoints de generacion de senales (Milestone 1)."""

from fastapi import APIRouter, Response

from app.routers.audio_http import wav_response
from app.schemas.signals import PinkNoiseRequest
from app.services.pink_noise import generate_pink_noise

router = APIRouter()


@router.post("/pink-noise")
async def pink_noise(req: PinkNoiseRequest) -> Response:
    """Genera ruido rosa y lo devuelve como archivo WAV.

    Parameters
    ----------
    req : PinkNoiseRequest
        Duracion en segundos y frecuencia de muestreo en Hz.

    Returns
    -------
    fastapi.Response
        Archivo WAV con el ruido rosa generado.
    """
    audio = generate_pink_noise(req.duration, req.sample_rate)
    return wav_response(audio, req.sample_rate, "pink_noise.wav")
