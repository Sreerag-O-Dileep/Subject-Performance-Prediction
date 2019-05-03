from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest, chi2
from sklearn import metrics
from sklearn.pipeline import Pipeline
from datamod import X_train, X_test, y_train, y_test
clf = GaussianNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("GNB Model Accuracy")
print(metrics.accuracy_score(y_test, y_pred))


def gnb(values):
    result = clf.predict(values)
    if result == 1:
        return 'good'
    elif result == 0:
        return 'bad'
