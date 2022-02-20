"""
Repository layer for flower service
"""
import pickle
from typing import Optional
from sklearn.ensemble import RandomForestClassifier


class FlowerClassifier:
    """
    Flower classifier singleton
    """
    iris_classifier: Optional[RandomForestClassifier] = None

    def __init__(self):
        raise Exception('Please use get_instance() method')

    @classmethod
    def get_instance(cls) -> RandomForestClassifier:
        """
        Class method to obtain singleton flower classifier
        """
        if cls.iris_classifier is None:
            with open('modules/flower/model.pkl', 'rb') as iris_model:
                cls.iris_classifier = pickle.load(iris_model)

        return cls.iris_classifier


class FlowerRepository:
    """
    Flower repository that uses the random forrest classifier
    """
    iris_classifier: RandomForestClassifier

    def __init__(self) -> None:
        self.iris_classifier = FlowerClassifier.get_instance()

    def get_flower_predictions(self, flower_attributes: list[list[float]]) -> list[int]:
        """
        Uses the random forrest classifier to generate predictions on flowers
        """
        predicted_flowers = self.iris_classifier.predict(
            flower_attributes).tolist()

        if not isinstance(predicted_flowers, list):
            raise Exception('Error generating flower prediction')

        return predicted_flowers

    def get_flower_prediction(self, flower_attributes: list[float]) -> int:
        """
        Uses the random forrest classifier to generate a prediction on flower
        """
        predicted_flower, *_ = self.get_flower_predictions([flower_attributes])

        return predicted_flower
