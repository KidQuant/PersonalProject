import quandl
import pandas as pd
import altair as alt
import numpy as np

alt.renderers.enable('altair_viewer')

quandl.ApiConfig.api_key = 'tJKSQn1pHLbyo1mu1wYn'

usGDP = quandl.get('FRED/A191RO1Q156NBEA')
usGDP.rename(columns={'Value': 'Real_GDP'}, inplace=True)
usGDP.reset_index(inplace=True)
