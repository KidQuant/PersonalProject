import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
import time

thisyear = '2017'
df = pd.read_csv('box' + thisyear +'2.csv')

names = df['name'].str.replace('\(.*\)','').str.replace(r'[\.\':,\?]','').str.replace('& ','').str.replace('- ','')
link1 = 'http://www.metacritic.com/movie/'
link2 = '/critic-reviews'

output_list = ['rank', 'moviename', 'meta_movie_name', 'release_date', 'total_score', 'num_crit', 'positive', 'mixed', 'negative',
                              'iscore', 'source', 'source_link', 'author', 'author_link', 'date', 'summary']
with open('mc' + thisyear +'.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow(output_list)

for i in range(0,len(names)):
    moviename = df.iloc[i]['name']
    rank = df.iloc[i]['rank']
    name = names[i].strip().lower()
    print (moviename, '^^^^^', name)
    link = link1 + name.replace(' ','-') + link2

    output_list = []
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        meta_movie_name = soup.find('div', class_='product_page_title upper pad_top2 pad_btm_half oswald').text.strip()
        num_crit = soup.find('span', class_='based_on').text.strip()
        error = 0
        print ('METANAME @@@@ ', meta_movie_name)
    except:
        error = 1
        print ('ERROR %%% ', name)
        output_list.append([rank, moviename, 'error'])

    if error == 0:
        release = soup.find('td', class_='left inset_right2 product_info lighter oswald upper pad_btm1')
        release_date = release.find('span', class_='release_date').text.replace('Release Date:','').strip()
        total_score = soup.find('td', class_='num_wrapper').text.strip()
        try:
            num_crit = soup.find('span', class_='based_on').text.strip()
            num_crit = int(re.search(r'\d+', num_crit).group())
        except:
            num_crit = ''
        try:
            positive = soup.find('div', class_='chart positive').text.strip()
            positive = int(re.search(r'\d+', positive).group())
            mixed = soup.find('div', class_='chart mixed').text.strip()
            mixed = int(re.search(r'\d+', mixed).group())
            negative = soup.find('div', class_='chart negative').text.strip()
            negative = int(re.search(r'\d+', negative).group())
        except:
            positive = ''
            mixed = ''
            negative = ''

        critics = soup.find_all('div', class_='review pad_top1 pad_btm1')
        for each in critics:
            iscore = each.find('div', class_='metascore_w').text.strip()
            try:
                source = each.find('span', class_='source').text.strip()
            except:
                source = ''
            try:
                source_link = 'http://www.metacritic.com/' + each.find('span', class_='source').a['href']
            except:
                source_link = ''
            try:
                author = each.find('span', class_='author').text.strip()
            except:
                author = ''
            try:
                author_link = 'http://www.metacritic.com/' + each.find('span', class_='author').a['href']
            except:
                author_link = ''
            try:
                date = each.find('span', class_='date').text.strip()
            except:
                date = ''
            try:
                summary = each.find('div', class_='summary').a.text.strip()
            except:
                summary = ''
            output_list.append([rank, moviename, meta_movie_name, release_date, total_score, num_crit, positive, mixed, negative,
                          iscore, source, source_link, author, author_link, date, summary])
    with open('mc' + thisyear +'.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
            w = csv.writer(csvfile)
            w.writerows(output_list)
    time.sleep(2)
