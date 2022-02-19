from sys import prefix
from fastapi import APIRouter
from pydantic import BaseModel
from .service import Flower_Service

router = APIRouter(prefix="/flower")


class Prediction_Request(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@router.post("/predict", response_model=str)
async def root(request: Prediction_Request):
    prediction_service = Flower_Service()
    return prediction_service.get_flower_prediction(request)
