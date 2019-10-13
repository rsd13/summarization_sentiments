import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import KFold
from sklearn.svm import SVC
from joblib import dump, load

def evaluacion(y_true, y_pred):
    recall = metrics.recall_score(y_true, y_pred, average='macro')
    #print("Recall: %f" % recall)
    precision = metrics.precision_score(y_true, y_pred, average='macro')
   #print("Precision: %f" % precision)
    f1_score = metrics.f1_score(y_true, y_pred, average='macro')
    #print("F1-score: %f" % f1_score)
    accuracy = metrics.accuracy_score(y_true, y_pred)
    return recall, precision, f1_score, accuracy


def SVMCross(X, y):
    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('SGDClassifier', SGDClassifier()),
    ])

    scores = []
    print(X, y)
    kf = KFold(n_splits=10, random_state=0, shuffle=True)
    for train, test in kf.split(X):
        print("go")
        X_train, X_test = X[train],  X[test]
        y_train, y_test = y[train], y[test]

        text_clf.fit(X_train, y_train)
        predicted = text_clf.predict(X_test)
        scores.append(evaluacion(y_test, predicted))

    recall = sum([x[0] for x in scores]) / len(scores)
    print("Averaged total recall", recall)
    precision = sum([x[1] for x in scores]) / len(scores)
    print("Averaged total precision", precision)
    f_score = sum([x[2] for x in scores]) / len(scores)
    print("Averaged total f-score", f_score)
    accuracy = sum([x[3] for x in scores]) / len(scores)
    print("Accuracy total ", accuracy)
    print(text_clf.predict(["No quisieron darnos una mesa por el mero hecho de tener un niño y llevar un carro. Se ve que les molestaba mucho hacer un hueco y poder perder dos sillas para otros dos clientes. No vayáis con vuestros niños pequeños. No son aptos para este restaurante"]))
    return text_clf



def open_dataset():
    """
    función que abre el dataset
    :return: dataset en formato DataFrame
    """
    dir_path = os.path.dirname(os.path.abspath(__file__)) + "/../datasets/global_clean.csv"
    return pd.read_csv(dir_path)




def train_model():
    data = open_dataset()
    X = data.frase
    y = data.emocion
    clf = SVMCross(X.values, y.values)

    dump(clf, 'filename.joblib')


train_model()
