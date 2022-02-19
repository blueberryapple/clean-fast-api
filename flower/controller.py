from fastapi import APIRouter
from pydantic import BaseModel
from .service import Flower_Service
from .repository import Flower_Repository

router = APIRouter(prefix="/flower")


class Prediction_Request(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@router.post("/predict", response_model=str)
async def root(request: Prediction_Request):
    flower_repository = Flower_Repository()
    prediction_service = Flower_Service(flower_repository)
    return prediction_service.get_flower_prediction(request)
