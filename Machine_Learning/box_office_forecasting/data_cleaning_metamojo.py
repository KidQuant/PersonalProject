import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time

thisyear = '2019'
df = pd.read_csv('mc' + thisyear + '.csv')

error = df[df['meta_movie_name'] == 'error']

noerror = df[df['meta_movie_name'] != 'error']

wrongdate = noerror[~noerror['release_date'].str.contains(thisyear)]

wrongdate = wrongdate.drop_duplicates(subset='rank', keep='first')

df_out = error.append(wrongdate)

df_out.to_csv('mc_error_'+thisyear+'.csv')
df_error = pd.read_csv('mc_error_'+ thisyear +'v2.csv')

df_merge = pd.merge(df, df_error, how = 'left', left_on=['rank'], right_on=['rank'])
