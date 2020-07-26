import altair as alt
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as ticker
import numpy as np
import time

%matplotlib inline
alt.renderers.enable('altair_viewer')

# Use for the most recent data release from JHU; otherwise change csv directory
today = time.strftime('%m-%d')

df = pd.read_csv(
    'covid-19-time-series-clean-complete-{}.csv'.format(today), parse_dates=['Date'])

df.head()

df.drop(columns=['Confirmed', 'Deaths', 'Active'], inplace=True)

new_df = df[(df['Province_State'] == 'Florida')
            | (df['Province_State'] == 'Texas')]
new_df.rename(columns={'Province_State': 'State'}, inplace=True)

new_df = new_df.reset_index().drop(columns=['index'])
new_df.sort_values(['State', 'Date'], inplace=True)


alt.Chart(new_df).mark_bar(opacity=0.7).encode(
    x='Date:T',
    y=alt.Y('New cases:Q', stack=None),
    color="State").configure_view(
    strokeWidth=0
).properties(
    title='Daily New Cases',
    width=600,
    height=300
).configure_title(
    fontSize=16,
    anchor='start'
)
