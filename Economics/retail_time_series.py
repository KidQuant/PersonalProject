import quandl
import pandas as pd
import altair as alt
import numpy as np

alt.renderers.enable('altair_viewer')

quandl.ApiConfig.api_key = 'tJKSQn1pHLbyo1mu1wYn'

retailSales = quandl.get('FRED/RRSFS')
retailSales.rename(columns={'Value': 'Retail Sales'}, inplace=True)
retailSales['Change in Retail Sales'] = retailSales['Retail Sales'].diff()
retailSales.reset_index(inplace=True)

base = alt.Chart(retailSales).encode(
    alt.X('Date:T',
        axis=alt.Axis(title='Source: U.S. Census Bureau'),
        textAlign='right')
)


bar = base.mark_bar().encode(
    alt.Y('Change in Retail Sales',
          axis=alt.Axis(format='$,.0f',
                        title='Monthly Change (In millions)')),
    color=alt.condition(
        alt.datum['Change in Retail Sales'] > 0,
        alt.value("green"),
        alt.value("red")
    )
)


line = base.mark_line(color='black').encode(
    alt.Y('Retail Sales',
          axis=alt.Axis(format='$,.0f',
                        title='Retail Sales (In millions)'),
          scale=alt.Scale(domain=[100000, 228000]))
)

alt.layer(bar, line).resolve_scale(
    y='independent'
).properties(
    title='Monthly and Aggregate U.S. Retail Sales',
    width=750,
    height=400
).configure_title(
    fontSize=16,
    anchor='start'
).configure_axis(
    labelFontSize=12
)
