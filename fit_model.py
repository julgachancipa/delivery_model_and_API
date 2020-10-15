from modeler.Modeler import Modeler

"""
Available classifiers:
    'GaussianNB'
    'DecisionTreeClassifier'
    'KNeighborsRegressor'
    'AdaBoostClassifier'
    'svm'
"""
clf = 'DecisionTreeClassifier'


def fit_model():
    Modeler().fit(clf=clf, scores=True)


if __name__ == '__main__':
    fit_model()
