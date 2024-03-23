import quandl
import pandas as pd
import altair as alt
import numpy as np
from altair import Scale, Color, Row, Column, Chart, Text

alt.renderers.enable('altair_viewer')

df = pd.read_csv('Data\Q2GDP.csv')

data = df[(df['Subject'] == 'Gross domestic product - expenditure approach')
          & (df['Period'] == 'Q2-2020') & (df['MEASURE'] == 'GYSA')]

data.reset_index(drop=True, inplace=True)
data.drop(columns=['SUBJECT', 'Subject', 'MEASURE', 'Measure',
                   'FREQUENCY', 'Frequency', 'TIME', 'PowerCode Code',
                   'PowerCode', 'Reference Period Code', 'Reference Period',
                   'Flag Codes', 'Flags', 'Unit Code', 'Unit'], inplace=True)
data.tail()

data['Value'] = data['Value'].apply(lambda x: x / 100)

data['Country'][30] = 'European Union'
data['Country'][28] = 'Euro Area'


selectedData = data.loc[data.Country.isin(
    ['United States', 'Spain', 'Germany', 'Italy', 'European Union', 'Canada', 'Portugal'])]

alt.Chart(selectedData).mark_bar().encode(
    x=alt.X('Country',
            title='Source: OECD Stat'),
    y=alt.Y('Value',
            axis=alt.Axis(format='.0%',
                          title='Q2 YoY Growth')),
    color=alt.condition(
        alt.datum.Country == 'United States',
        alt.value('red'),
        alt.value('lightgrey')
    )
).properties(
    title='Coronavirus Effect on Q2 GDP Growth',
    width=700,
    height=300
).configure_axis(
    labelFontSize=13
).configure_title(
    fontSize=18,
    anchor='start'
)
