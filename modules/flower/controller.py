"""
Controller layer of application
"""
from typing import TypedDict
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from .service import FlowerService
from .repository import FlowerRepository

router = APIRouter(prefix="/flower", tags=['flower'])


class Services(TypedDict):
    """
    Defines all service dependencies
    """
    flower_service: FlowerService


def get_services(flower_repository: FlowerRepository = Depends()) -> Services:
    """
    Gets all service dependencies
    """
    return {
        'flower_service': FlowerService(flower_repository)
    }


class PredictionRequest(BaseModel):
    """
    Defines the request payload schema for flower prediction
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@router.post("/predict", response_model=str)
async def predict_flower(request: PredictionRequest, services: Services = Depends(get_services)):
    """
    Predicts flower given petal and sepal measurements using a random forrest classifier
    """
    flower_service = services['flower_service']

    return flower_service.get_flower_prediction({
        'petal_length': request.petal_length,
        'petal_width': request.petal_width,
        'sepal_length': request.sepal_length,
        'sepal_width': request.sepal_width
    })
