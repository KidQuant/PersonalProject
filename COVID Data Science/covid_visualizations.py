
# %%
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

variable = 'New Deaths'

global_df = pd.read_csv(
    'covid-19-time-series-clean-global-{}.csv'.format(today), parse_dates=['Date'], usecols=['Date', 'Country/Region', variable])

us_df = pd.read_csv('covid-19-time-series-clean-us-{}.csv'.format(today),
                    parse_dates=['Date'], usecols=['Date', 'Province_State', variable])

global_df.head()
us_df.head()

area = 'Sweden'

area_df = global_df[global_df['Country/Region'] == area]

area_df = area_df.reset_index().drop(columns=['index'])

area_df['7-Day Moving Average'] = area_df[variable].rolling(7).mean()

f = alt.Chart().mark_bar().encode(
    x="Date:T",
    y="{}:Q".format(variable)
)

c = alt.Chart().mark_line(color='red', strokeDash=[5, 1]).transform_window(
    rolling_mean='mean(variable:Q)'.format(variable),
    frame=[-7, 0],
    groupby=['Country/Region']
).encode(
    x='Date:T',
    y=alt.Y('7-Day Moving Average:Q')
)


alt.layer(f, c, data=area_df).properties(
    title='Daily {} {}'.format(variable, area),
    width=600,
    height=300
).configure_title(
    fontSize=16,
    anchor='start'
)
