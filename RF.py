from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import RandomForestClassifier
from datamod import X_train, X_test, y_train, y_test
clf =  RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Random Forest Model Accuracy")
print(metrics.accuracy_score(y_test,y_pred))
def rf(values):
    result = clf.predict(values)
    if result == 1:
        return 'good'
    elif result == 0:
        return 'bad'