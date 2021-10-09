import uvicorn
from fastapi import FastAPI, APIRouter, Depends
from starlette.middleware.cors import CORSMiddleware
from setting.database import get_db_sync
from src.routes import TaxCalculator

db = get_db_sync()


app = FastAPI(response_model_exclude_unset=True)
origins = ["http://localhost:8080", "http://localhost:8081"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(TaxCalculator.router, prefix="/taxCal", tags=["tax"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
