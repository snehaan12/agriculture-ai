from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import crop_health, disease, irrigation

app = FastAPI(
    title="FarmAI Backend",
    description="Backend for precision agriculture application",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(crop_health.router, prefix="/api/v1")
app.include_router(disease.router, prefix="/api/v1")
app.include_router(irrigation.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "FarmAI Backend Service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)