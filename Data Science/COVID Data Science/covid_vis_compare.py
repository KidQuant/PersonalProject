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

us_df = pd.read_csv(
    'Data/covid-19-time-series-clean-us-{}.csv'.format(today), parse_dates=['Date'], usecols=['Date', 'Province_State', 'New Deaths']
)

us_df.rename(columns={'Province_State': 'Region'}, inplace=True)

# global_df = pd.read_csv(
#     'covid-19-time-series-clean-global-{}.csv'.format(today), parse_dates=['Date'], usecols=['Date', 'Country/Region', 'New Cases']
# )
#
#
# global_df.rename(columns={'Country/Region': 'Region'}, inplace=True)

state_1 = us_df[us_df['Region'] == 'Florida']
state_2 = us_df[us_df['Region'] == 'New York']
# country_1 = global_df[global_df['Region'] == 'Denmark']

new_df = pd.concat([state_1, state_2], axis=0, sort=False)

new_df = new_df.reset_index().drop(columns=['index'])

alt.Chart(new_df).mark_bar(opacity=0.7).encode(
    x=alt.X(
        'Date:T',
        title='Source: JHU Covid Dashboard'),
    y=alt.Y(
        'New Deaths:Q',
        stack=None,
        title='New Fatalities'),
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

state_1.tail(16)
