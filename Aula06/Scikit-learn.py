import numpy as np

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("../Csv/temperature.csv")

x,y = df[['month']].values, df[['City']].values
#print("X:\n",x)
#print("Y:\n",y)

le=LabelEncoder()
y = le.fit_transform(y.ravel())
#print("Y:\n",y)

clf = LogisticRegression()
clf.fit(x,y)

x_test = np.linspace(start=0, stop=45, num=100).reshape(-1, 1)
y_pred = clf.predict(x_test)

y_pred = le.inverse_transform(y_pred)