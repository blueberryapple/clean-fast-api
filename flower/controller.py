from typing import TypedDict
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from .service import FlowerService
from .repository import FlowerRepository

router = APIRouter(prefix="/flower", tags=['flower'])


class Services(TypedDict):
    flower_service: FlowerService


def get_services(flowerRepository: FlowerRepository = Depends()) -> Services:
    return {
        'flower_service': FlowerService(flowerRepository)
    }


class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@router.post("/predict", response_model=str)
async def root(request: PredictionRequest, services: Services = Depends(get_services)):
    flower_service = services.get('flower_service')
    return flower_service.get_flower_prediction(request)
