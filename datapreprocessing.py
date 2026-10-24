import pandas as pd
import numpy as np
data = pd.read_csv('Data.csv')
print(data.info())
#1. clean data - datasets should not contain missing values
#nan = not a number
print(data.isnull().sum())
from sklearn.impute import SimpleImputer
SI = SimpleImputer(missing_values=np.nan, strategy="mean")
SI.fit(data.iloc[:, 1:3])
data.iloc[:, 1:3] = SI.transform(data.iloc[:, 1:3])
print(data)
#2. separating features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
#3. split into training and testing
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=20)