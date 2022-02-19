import pickle
from sklearn.ensemble import RandomForestClassifier


class FlowerRepository:
    iris_classifier: RandomForestClassifier

    def __init__(self) -> None:
        with open('flower/model.pkl', 'rb') as iris_model:
            self.iris_classifier = pickle.load(iris_model)

    def get_flower_prediction(self, flower_attributes: list[float]) -> list[int]:
        predicted_flower = self.iris_classifier.predict(
            [flower_attributes]).tolist()

        if not isinstance(predicted_flower, list):
            raise Exception('Error generating flower prediction')

        return predicted_flower
