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


# us_df = pd.read_csv(
#     'covid-19-time-series-clean-us-{}.csv'.format(today), parse_dates=['Date'], usecols=['Date', 'Province_State', 'New Deaths']
# )

global_df = pd.read_csv(
    'covid-19-time-series-clean-global-{}.csv'.format(today), parse_dates=['Date'], usecols=['Date', 'Country/Region', 'New Deaths']
)

# us_df.rename(columns={'Province_State': 'Region'}, inplace=True)
global_df.rename(columns={'Country/Region': 'Region'}, inplace=True)

florida = us_df[us_df['Region'] == 'Arizona']
newyork = us_df[us_df['Region'] == 'New York']
# italy = global_df[global_df['Region'] == 'Italy']

new_df = pd.concat([florida, newyork], axis=0, sort=False)

new_df = new_df.reset_index().drop(columns=['index'])

alt.Chart(new_df).mark_bar(opacity=0.7).encode(
    x='Date:T',
    y=alt.Y('New Deaths:Q', stack=None),
    color="Region").configure_view(
    strokeWidth=00
).properties(
    title='Daily New Fatalities',
    width=600,
    height=300
).configure_title(
    fontSize=16,
    anchor='start'
)
