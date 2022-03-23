import IPython
import altair as alt
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as ticker
import numpy as np
import time
%matplotlib inline

alt.renderers.enable('altair_viewer')


def black_marks():
    return {
        'config': {
            'view': {
                'height': 300,
                'width': 600,
            },
            'mark': {
                'color': 'black',
            }
        }
    }


# register the custom theme under a chosen name
alt.themes.register('black_marks', black_marks)
# enable the newly registered theme
alt.themes.enable('black_marks')

today = time.strftime('%m-%d')

variable1 = 'New Cases'
variable2 = 'New Deaths'

global_df = pd.read_csv(
    'Data/covid-19-time-series-clean-global-{}.csv'.format(today), parse_dates=['Date'], usecols=['Date', 'Country/Region', variable1, variable2])

global_df.rename(columns={'Country/Region': 'Region'}, inplace=True)

area_1 = 'Sweden'
area_2 = 'France'

area_df1 = global_df[global_df['Region'] == area_1]
area_df2 = global_df[global_df['Region'] == area_2]

area_df1['7-Day Moving Average'] = area_df1['New Cases'].rolling(7).mean()
area_df2['7-Day Moving Average'] = area_df2['New Cases'].rolling(7).mean()


chart_france = alt.Chart(area_df1).mark_bar().encode(
    x=alt.X('Date:T', title=None)
).properties(
    width=400,
    height=350
)

france_bars = chart_france.mark_bar().encode(
    x=alt.X('Date:T', title='France'),
    y=alt.Y('New Cases:Q', title='New Cases')
)

france_line = chart_france.mark_line(color='red', strokeDash=[5, 1]).encode(
    y=alt.Y('7-Day Moving Average:Q', title='7-Day Moving Average')
)

chart_germany = alt.Chart(area_df2).mark_bar().encode(
    x=alt.X('Date:T', title=None)
).properties(
    width=400,
    height=350
)

germany_bars = chart_germany.mark_bar().encode(
    y=alt.Y('New Cases:Q', title='New Case')
)

germany_line = chart_germany.mark_line(color='red', strokeDash=[5, 1]).encode(
    y=alt.Y('7-Day Moving Average:Q', title='7-Day Moving Average')
)

((france_bars + france_line).properties(title='France') | (germany_bars + germany_line).properties(title='Germany')).properties(
    title='COVID-19 Cases Re-emerging in Europe',
).configure_title(
    fontSize=18
)
