import pandas as pd
data = pd.read_csv('titanic.csv')
print(data.info())
print(data.shape) #rows and columns as a tuple
print(data.head()) #first 5 is the default parameter, can pass other numbers for no. of rows
print(data.tail())
print(data.dtypes) #data types
print(data.describe()) #statistics, description

print((data[['Name', 'Age']])) #several columns
#filtering the data
print(data['Age'])
print(data[data['Age']>35]['Name'])
#records of those who belong to class 2 or 3
print(data[(data['Pclass']==2)|(data['Pclass']==3)]) # & and | or
#data of male passengers of class 2
print(data[(data['Pclass']==2)&(data['Sex']=='male')])
#value_count: find how many male and female passengers there are
print(data['Sex'].value_counts())

#aggregate functions take several input values and output 1 value, and all (exccept count, omn any data type) work on numerical data
# count(), min(), max(), mean(), sum(), std()
# count of passenger fare
print(data['Fare'].count())
print(data['Fare'].min())
print(data['Fare'].max())
print(data['Fare'].mean())
print(data['Fare'].sum())
print(data['Fare'].std())

print(data[data['Sex']=='male']['Fare'].mean())
print(data[data['Sex']=='female']['Fare'].mean())

print(data.groupby('Sex')['Fare'].mean()) #group data by column e.g. sex
print(data.groupby(['Sex', 'Pclass'])['Fare'].mean()) #whenever you apply groupby function, you can only apply the aggregate function after, no other function
