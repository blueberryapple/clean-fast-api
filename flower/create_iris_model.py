import pickle

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

iris = datasets.load_iris()
classifier = RandomForestClassifier()
classifier.fit(iris.data, iris.target)

with open('flower/model.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)
