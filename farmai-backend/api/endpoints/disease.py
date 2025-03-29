from fastapi import APIRouter, UploadFile, File, HTTPException
from models.disease import predict_disease
from schemas.response import DiseaseResponse
from api.utils import validate_image_file

router = APIRouter()

@router.post("/analyze-leaf", response_model=DiseaseResponse)
async def analyze_leaf(file: UploadFile = File(...)):
    validate_image_file(file)
    
    try:
        contents = await file.read()
        return predict_disease(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))