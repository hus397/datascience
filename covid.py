#province, country, confirmed, recovered, deaths
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import plotly
import plotly.express as px
import plotly.graph_objects as go
data = pd.read_csv('covid_data.csv')
usable_data = data[['Province_State', 'Country_Region', 'Confirmed', 'Recovered', 'Deaths']]
print(usable_data)
us_data = usable_data[usable_data['Country_Region']=='US']
print(us_data['Confirmed'].sum())
#top 10 countries with highest number of deaths
grouped_data = usable_data.groupby('Country_Region')['Confirmed'].sum().sort_values(ascending=False).head(10)
"""mp.bar(grouped_data.index, grouped_data.values)
mp.show()
bar_graph = px.bar(grouped_data, grouped_data.index, grouped_data.values, color='Confirmed', color_continuous_scale=px.colors.sequential.matter, title='COVID cases')
bar_graph.write_html('10_COVID.html', auto_open = True)"""
#top 10 states in the USA with the highest number of deaths
usg_data = us_data.groupby('Province_State')['Confirmed'].sum().sort_values(ascending=False).head(10)
bar_graph = px.bar(usg_data, usg_data.index, usg_data.values, color='Confirmed', color_continuous_scale=px.colors.sequential.matter, title='COVID cases')
"""bar_graph.write_html('US_COVID.html', auto_open = True)"""
usd_data = us_data.groupby('Province_State')['Deaths'].sum().sort_values(ascending=False).head(10)
"""go_graph = go.Figure(data=[
    go.Bar(name='Confirmed Cases', x=usg_data.index, y=usg_data.values), 
    go.Bar(name='Deaths', x=usd_data.index, y=usd_data.values)
])
go_graph.write_html('USCOVID.html', auto_open = True)
print(usd_data, usg_data)"""
brazil_data = data.groupby('Country_Region').get_group('Brazil')
confirmed_cases = brazil_data.nlargest(10, 'Confirmed')
go2_graph = go.Figure(data=[
    go.Bar(name='Confirmed Cases', x=confirmed_cases['Province_State'], y=confirmed_cases['Confirmed']), 
    go.Bar(name='Deaths', x=confirmed_cases['Province_State'], y=confirmed_cases['Deaths']),
    go.Bar(name='Active Cases', x=confirmed_cases['Province_State'], y=confirmed_cases['Deaths'])
])
go2_graph.update_layout(title='COVID in Brazil', height=600)
go2_graph.write_html('BCOVID.html', auto_open = True)
