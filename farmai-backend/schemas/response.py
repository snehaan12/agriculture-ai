# schemas/request.py
from pydantic import BaseModel
from datetime import date
from typing import List

class CropHealthRequest(BaseModel):
    start_date: date
    end_date: date
    coordinates: List[List[float]]

class IrrigationRequest(BaseModel):
    field_id: str
    soil_moisture: float
    weather_forecast: str