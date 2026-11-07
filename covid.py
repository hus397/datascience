#province, country, confirmed, recovered, deaths
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import plotly
import plotly.express as px
data = pd.read_csv('covid_data.csv')
usable_data = data[['Province_State', 'Country_Region', 'Confirmed', 'Recovered', 'Deaths']]
print(usable_data)
us_data = usable_data[usable_data['Country_Region']=='US']
print(us_data['Confirmed'].sum())
#top 10 countries with highest number of deaths
grouped_data = usable_data.groupby('Country_Region')['Confirmed'].sum().sort_values(ascending=False).head(10)
"""mp.bar(grouped_data.index, grouped_data.values)
mp.show()"""
bar_graph = px.bar(grouped_data, grouped_data.index, grouped_data.values, color='Confirmed', color_continuous_scale=px.colors.sequential.matter, title='COVID cases')
bar_graph.write_html('10_COVID.html', auto_open = True)

#deaths, recover by country
#deaths, country, confirmed by state, scatter graph

