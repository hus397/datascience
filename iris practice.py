"""1. Display the first 5 rows
Write code to display the first 5 rows of df.
2. Display the last 10 rows
Which Pandas function can you use?
3. Find the number of rows and columns
Display the shape of the DataFrame.
4. Display all column names
Write code to print the column names.
5. Find the data types
Display the datatype of every column.
6. Find missing values
Write code to check whether any column contains missing values.
7. Find basic statistics
Use Pandas to display:
mean
standard deviation
minimum
maximum
for the numerical columns."""
import pandas as pd
data = pd.read_csv('iris.csv')
print(data.head())
print(data.tail(10))
print(data.shape) 
print(data.info())
print(data.dtypes)
print(data.agg({"sepal_length":["min", "max", "sum", "mean", "median", "std"], "sepal_width":["min", "max", "sum", "mean", "median", "std"], "petal_length":["min", "max", "sum", "mean", "median", "std"], "petal_width":["min", "max", "sum", "mean", "median", "std"]}))
print(data.isna().sum()) 

"""22. Find the maximum petal length for each species
For each species, find its maximum:
petal length (cm)
23. Find the minimum sepal width for each species
Group by species and find the minimum:
sepal width (cm)
24. Count flowers in each species
Find how many flowers belong to each value of:
species"""
print(data[data["species"]=="setosa"].agg([max, min]))
print(data[data["species"]=="versicolor"].agg([max, min]))
print(data[data["species"]=="virginica"].agg([max, min]))
print(data[data['species']=="setosa"].count())
print(data[data['species']=="versicolor"].count())
print(data[data['species']=="virginica"].count())
"Find the average petal area for each species "
"and sort the result from highest to lowest."
data["petal_area"] = data['petal_length']*data["petal_width"]
print(data.groupby(["species"])["petal_area"].mean().sort_values(ascending=False))
