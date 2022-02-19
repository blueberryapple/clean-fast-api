from .repository import FlowerRepository


class FlowerAttributes:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


flowers: list[str] = ['iris-setosa', 'iris-versicolor', 'iris-virginia']


class FlowerService:
    flower_repository: FlowerRepository

    def __init__(self, flower_repository) -> None:
        self.flower_repository = flower_repository

    def get_flower_prediction(self, flower_attributes: FlowerAttributes) -> str:
        flower_values = [flower_attributes.sepal_length, flower_attributes.sepal_width,
                         flower_attributes.petal_length, flower_attributes.petal_width]

        flower_prediction, *_ = self.flower_repository.get_flower_prediction(
            flower_values)

        return flowers[flower_prediction]
