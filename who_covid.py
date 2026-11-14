import pandas as pd
import numpy as np
data = pd.read_csv('WHO-COVID-19-global-data.csv')
data.columns=('DateReported','Country_code','Country','WHO_region','New_cases','Cumulative_cases','New_deaths','Cumulative_deaths')
data['DateReported']=pd.to_datetime(data['DateReported'])
print(data.info())
#how many deaths reported on a particular date
print(data.groupby('DateReported')['New_deaths'].sum())


