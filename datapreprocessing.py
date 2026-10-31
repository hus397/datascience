import pandas as pd
import numpy as np
data = pd.read_csv('Data.csv')
#print(data.info())
#1. clean data - datasets should not contain missing values
#nan = not a number
#print(data.isnull().sum())
from sklearn.impute import SimpleImputer
SI = SimpleImputer(missing_values=np.nan, strategy="mean")
SI.fit(data.iloc[:, 1:3])
data.iloc[:, 1:3] = SI.transform(data.iloc[:, 1:3])
#print(data)
#2. separating features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
#3. encoding - convert non numeric columns into numeric ones - purchase and country
#label encoding - assign labels to every value
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
y = LE.fit_transform(y)
#functions: fit - using data to train the model, transform - using previous knowledge to make transformation, fit_transform - read from the data and then make a modification to the same dataset
#one-hot encoding - go through data, create that many columns in dataset in alphabetical order
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
CT = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(CT.fit_transform(X))
#print(X)
#print(y)
#4, feature scaling (when the range appears to be too big)
from sklearn.preprocessing import StandardScaler
SS = StandardScaler()
X = SS.fit_transform(X[:, 2:])
#print(X)
#5. split into training and testing
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=20)
print(xtrain, xtest, ytrain, ytest)
