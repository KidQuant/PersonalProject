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

#Getting MC true matching

df_error = pd.read_csv('mc_error_'+ thisyear +'.csv')
df = pd.read_csv('mc'+ thisyear +'.csv')
df_merge = pd.merge(df, df_error, how = 'left', left_on=['rank'], right_on=['rank'])
df_right = df_merge[df_merge.moviename_y.isnull()]

output_list = []
for i in range(0, len(df_error)):
    moviename = df_error.iloc[i]['moviename']
    rank = df_error.iloc[i]['rank']
    name = df_error.iloc[i]['link']
    print(moviename, '^^^^^', name)
    link1 = 'http://www.metacritic.com/movie/'
    link2 = '/critic-reviews'
    link = link1 + name + link2

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        meta_movie_name = soup.find('div', class_='product_page_title upper pad_top2 pad_btm_half oswald').text.strip()
        num_crit = soup.find('span', class_='based_on').text.strip()
        error = 0
        print('METANAME @@@@', meta_movie_name)
    except:
        error = 1
        print('ERROR %%%%', name)
        output_list.append([rank, moviename, 'error'])

    if error == 0:
        release = soup.find('td', class_='left inset_right2')
