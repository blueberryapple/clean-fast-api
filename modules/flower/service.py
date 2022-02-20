"""
Service layer for flower service
"""
from typing import TypedDict
from .repository import FlowerRepository


class FlowerAttributes(TypedDict):
    """
    Flower attributes required to make a prediction on flower
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


flowers: list[str] = ['iris-setosa', 'iris-versicolour', 'iris-virginica']


class FlowerService:
    """
    Flower service to predict flower
    """
    flower_repository: FlowerRepository

    def __init__(self, flower_repository: FlowerRepository) -> None:
        self.flower_repository = flower_repository

    def get_flower_prediction(self, flower_attributes: FlowerAttributes) -> str:
        """
        Gets flower prediction from the flower repository
        """
        flower_values = [flower_attributes['sepal_length'], flower_attributes['sepal_width'],
                         flower_attributes['petal_length'], flower_attributes['petal_width']]

        flower_prediction = self.flower_repository.get_flower_prediction(
            flower_values)

        return flowers[flower_prediction]
