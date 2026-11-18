
"""Router para utilidades de procesamiento de señales (Milestone 3)."""

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.routers.audio_http import uploaded_file
from app.schemas.utils import SchroederResponse, SmoothingMethod, SmoothingResponse
from app.services.acoustic_parameters import apply_schroeder_integral, apply_smoothing
from app.services.signal_utils import load_audio

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

router = APIRouter()

@router.post("/smoothing", response_model=SmoothingResponse)
async def smoothing(
    file: UploadFile = File(...),  # noqa: B008
    method: SmoothingMethod = Form(SmoothingMethod.HILBERT),  # noqa: B008
    window_ms: float = Form(10, gt=0, le=100),
):
    """Recibe un audio y devuelve su envolvente suavizada."""

    with uploaded_file(file) as path:
        try:
            signal, fs = load_audio(path)
        except ValueError as e:
            raise HTTPException(
                status_code=422, detail=f"No es un audio válido: {e}"
            ) from e

    try:
        envelope = apply_smoothing(signal, fs, method.value, window_ms)
    except ValueError as e:
        raise HTTPException(
            status_code=422, detail=f"Parámetros inválidos: {e}"
        ) from e

    step = max(1, round(fs / 1000))

    return SmoothingResponse(
        method=method,
        window_ms=window_ms,
        sample_rate=fs,
        time_step=step / fs,
        envelope=envelope[::step].tolist(),
    )

@router.post("/schroeder", response_model=SchroederResponse)
async def schroeder(file: UploadFile = File(...)):

    """Recibe un audio y devuelve su integral de Schroeder."""

    with uploaded_file(file) as path:
        try:
            scresponse = apply_schroeder_integral(path)
        except ValueError as e:
            raise HTTPException(
                status_code=422, detail=f"No es un audio válido: {e}"
            ) from e

    return SchroederResponse(
        scresponse=scresponse,
    )
