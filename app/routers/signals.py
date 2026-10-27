"""Endpoints de generacion de senales (Milestone 1)."""

from fastapi import APIRouter, Response, HTTPException

from app.routers.audio_http import wav_response
from app.schemas.signals import PinkNoiseRequest
from app.schemas.signals import SineSweepRequest
from app.services.pink_noise import generate_pink_noise
from app.services.sine_sweep import generate_sine_sweep_pair


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

# arriba del archivo: from fastapi import APIRouter, HTTPException
#                     from app.services.sine_sweep import generate_sine_sweep_pair

@router.post("/sine-sweep")                         # POST /api/v1/signals/sine-sweep
async def sine_sweep(req: SineSweepRequest):
    if req.start_freq >= req.end_freq:
        raise HTTPException(status_code=400, detail="start_freq tiene que ser menor que end_freq")
    
    sweep, inverse_filter = generate_sine_sweep_pair(
        req.duration, req.start_freq, req.end_freq, req.sample_rate
    )

    if req.inverse: 
        return wav_response(inverse_filter, req.sample_rate, "filtro_inverso.wav")
    else:
        return wav_response(sweep, req.sample_rate, "sine_sweep.wav")
    
    # devolver con wav_response el sweep o el filtro inverso, según req.inverse