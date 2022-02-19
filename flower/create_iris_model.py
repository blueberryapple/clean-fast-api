"""
Creates the flower random forrest classifier
"""
import pickle
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

iris_data, iris_target = datasets.load_iris(return_X_y=True)

classifier = RandomForestClassifier()
classifier.fit(iris_data, iris_target)

with open('flower/model.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)
