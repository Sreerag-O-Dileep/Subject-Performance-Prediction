import pandas as pd
import numpy as np
df = pd.read_csv("student-mat.csv", sep=";")
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
le=LabelEncoder()
fselect=df.iloc[:,:]
for column in fselect:
    df[column]=le.fit_transform(df[column])
for i, row in df.iterrows(): 
        if row["s1"] >= 10:
            df["s1"][i] = 1
        else:
            df["s1"][i] = 0

        if row["s2"] >= 10:
            df["s2"][i] = 1
        else:
            df["s2"][i] = 0

        if row["sem"] >= 10:
            df["sem"][i] = 1
        else:
            df["sem"][i] = 0
y = df.pop("sem")
X = df
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=17)