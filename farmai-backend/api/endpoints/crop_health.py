from fastapi import APIRouter, Depends, HTTPException
from datetime import date
from models.crop_health import analyze_crop_health
from schemas.request import CropHealthRequest
from schemas.response import CropHealthResponse

router = APIRouter()

@router.post("/crop-health", response_model=CropHealthResponse)
async def get_crop_health(request: CropHealthRequest):
    try:
        result = analyze_crop_health(
            start_date=request.start_date,
            end_date=request.end_date,
            coordinates=request.coordinates
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))