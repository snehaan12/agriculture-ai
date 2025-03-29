from fastapi import APIRouter, HTTPException
from models.irrigation import get_irrigation_recommendation
from schemas.request import IrrigationRequest
from schemas.response import IrrigationResponse

router = APIRouter()

@router.post("/irrigation", response_model=IrrigationResponse)
async def get_irrigation(request: IrrigationRequest):
    try:
        return get_irrigation_recommendation(
            field_id=request.field_id,
            soil_moisture=request.soil_moisture,
            weather_forecast=request.weather_forecast
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))