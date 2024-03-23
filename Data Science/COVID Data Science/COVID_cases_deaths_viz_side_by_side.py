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

area = 'Italy'

area_df = global_df[global_df['Region'] == area]

area_df['7-DMA (New Cases)'] = area_df['New Cases'].rolling(7).mean()
area_df['7-DMA (New Deaths)'] = area_df['New Deaths'].rolling(7).mean()

chart = alt.Chart(area_df).encode(
    x=alt.X('Date:T', title=None)
)

case_bars = chart.mark_bar().encode(
    y=alt.Y('New Cases:Q', title='New Confirmed Cases')
).properties(
    width=600,
    height=200
)

cases_line = chart.mark_line(color='red', strokeDash=[5, 1]).encode(
    y=alt.Y('7-DMA (New Cases)', title='7-Day Moving Average')
)

deaths_bar = chart.mark_bar().encode(
    y=alt.Y('New Deaths:Q', title='New Confirmed Fatalities'
            ),
).properties(
    width=600,
    height=200
)

deaths_line = chart.mark_line(color='red', strokeDash=[5, 1]).encode(
    y=alt.Y('7-DMA (New Deaths)', title='7-Day Moving Average')
)

((case_bars + cases_line) & (deaths_bar + deaths_line)).configure_axis(
    labelFontSize=13
).properties(
    title='Sweden: New Daily Cases and Fatalities'
).configure_title(
    fontSize=18
)

(case_bars + cases_line).configure_axis(
    labelFontSize=13
).properties(
    title='Sweden: New Daily Cases and Fatalities'
).configure_title(
    fontSize=18
)
