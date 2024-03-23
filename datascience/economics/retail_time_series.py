import quandl
import pandas as pd
import altair as alt
import numpy as np

alt.renderers.enable('altair_viewer')

quandl.ApiConfig.api_key = 'tJKSQn1pHLbyo1mu1wYn'

retailSales = quandl.get('FRED/RSNSR')
retailSales.rename(columns={'Value': 'Online Sales'}, inplace=True)
retailSales['Change in Online Sales'] = retailSales['Online Sales'].diff()
retailSales.reset_index(inplace=True)

base = alt.Chart(retailSales).encode(
    alt.X('Date:T',
          axis=alt.Axis(title='Source: U.S. Census Bureau'))
)


bar = base.mark_bar().encode(
    alt.Y('Change in Online Sales',
          axis=alt.Axis(format='$,.0f',
                        title='Monthly Change (In millions)')),
    color=alt.condition(
        alt.datum['Change in Online Sales'] > 0,
        alt.value("green"),
        alt.value("red")
    )
)


line = base.mark_line(color='black').encode(
    alt.Y('Online Sales',
          axis=alt.Axis(format='$,.0f',
                        title='Retail Sales (In millions)'),
          scale=alt.Scale(domain=[0, 90000]))
)

alt.layer(bar, line).resolve_scale(
    y='independent'
).properties(
    title='Monthly and Aggregate U.S. Online Sales',
    width=750,
    height=450
).configure_title(
    fontSize=18,
    anchor='start'
).configure_axis(
    labelFontSize=12
)
