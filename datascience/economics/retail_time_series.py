import altair as  alt
from fredapi import Fred

# alt.renderers.enable('altair_viewer')
# quandl.ApiConfig.api_key = 'CTnhpzRXRtpR9w1bU7ae'

fred = Fred(api_key="c2349ff4a2a3a64e1f7c38d82e02b705")
retailSales = fred.get_series("RSNSR")
retailSales = retailSales.to_frame()
retailSales.reset_index(inplace=True)
retailSales.rename(columns={0:'Online Sales', 'index':'Date'}, inplace=True)
retailSales['Change in Online Sales'] = retailSales['Online Sales'].diff()

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
          scale=alt.Scale(domain=[0, 120000]))
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
