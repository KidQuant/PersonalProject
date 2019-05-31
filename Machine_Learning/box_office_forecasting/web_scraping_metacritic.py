import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
import time

thisyear = '2019'
df = pd.read_csv('box'+ thisyear +'.csv')

names = df['name'].str.replace('\(.*\)','').str.replace(r'[\.\':,\?]','').str.replace('& ','').str.replace('- ','')
link1 = 'http://www.metacritic.com/movie/'
link2 = '/critic-reviews'

output_list = ['rank', 'moviename', 'meta_movie_name', 'release_date', 'total_score', 'num_crit', 'positive', 'mixed', 'negative',
'iscore', 'source', 'source_link', 'author', 'author_link', 'date', 'summary']

with open('mc' + thisyear + '.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(output_list)

for i in range(0, len(names)):
    moviename = df.iloc[i]['name']
    rank = df.iloc[i]['rank']
    name = names[i].strip().lower()
    print(moviename, '^^^^^', name)

    output_list  = []
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(link, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        meta_movie_name = soup.find('div', class_='product_page_title upper pad_top2 pad_btm_half oswald').text.strip()
        num_crit = soup.find('span', class_ ='based_on').text.strip()
        error = 0
        print('METANAME @@@@ 'meta_movie_name)
    except:
        error = 1
        print('ERROR %%% ', name)
        
