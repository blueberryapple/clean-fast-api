import pickle

from sklearn import datasets
from sklearn.utils import Bunch
from sklearn.ensemble import RandomForestClassifier

iris = datasets.load_iris()

if not isinstance(iris, Bunch):
    raise Exception('Iris dataset is not an instance of Bunch')

classifier = RandomForestClassifier()
classifier.fit(iris.data, iris.target)

with open('flower/model.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)
