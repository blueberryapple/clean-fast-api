import pickle
from sklearn.ensemble import RandomForestClassifier


class Flower_Repository:
    iris_classifier: RandomForestClassifier

    def __init__(self) -> None:
        with open('flower/model.pkl', 'rb') as iris_model:
            self.iris_classifier = pickle.load(iris_model)

    def get_flower_prediction(self, flower_attributes: list[float]):
        return self.iris_classifier.predict([flower_attributes])
