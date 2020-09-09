import numpy as np
import pandas as pd
import requests
import json
import time

today = time.strftime("%Y%m%d")

url = 'http://ww11.doh.state.fl.us/comm/_partners/covid19_report_archive/state_linelist_'

filepath = url + today + ".xlsx"

filepath = url + "20200903" + ".xlsx"

with pd.ExcelFile(filepath) as xls:
    df1 = pd.read_excel(xls, 'Cases', skiprows=[0, 1, 2])
    df2 = pd.read_excel(xls, 'Deaths', skiprows=[0, 1, 2, 3])

df2.sort_values('Date case counted', inplace=True)


df2[df2['Newly identified death'] == 'Yes'].sort_values(
    by='Date case counted', ascending=False)

df2[df2['Newly identified death'] == 'Yes'].count()

df2[df2['Date case counted'].betweeen(
    '2020-07-29 23:59:59.555', '2020-07-28 23:59:59.555')].count()


df1.sort_values('Date case counted', inplace=True)
df1.tail()
df2[df2['Date case counted'] > '2020-08-17 23:55:57.553'].count()

df2['Date case counted'].between(
    '2020-07-27 23:59:59.555', '2020-07-27 23:59:59.555')
