import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time

thisyear = '2017'
df = pd.read_csv('mc'+ thisyear +'.csv')

error = df[df['meta_movie_name'] == 'error']

noerror = df[df['meta_movie_name'] != 'error']

wrongdate = noerror[~noerror['release_date'].str.contains(thisyear)]

wrongdate = wrongdate.drop_duplicates(subset='rank', keep="first")

df_out = error.append(wrongdate)

df_out.to_csv('mc_error_'+thisyear+'.csv')

#Getting MC true matching

df_error = pd.read_csv('mc_error_'+ thisyear +'v2.csv')
df= pd.read_csv('mc'+ thisyear+'.csv')

df_merge = pd.merge(df, df_error,  how='left', left_on=['rank'], right_on = ['rank'])
df_right = df_merge[df_merge.moviename_y.isnull()]

output_list = []
for i in range(0,len(df_error)):
    moviename = df_error.iloc[i]['moviename']
    rank = df_error.iloc[i]['rank']
    name = df_error.iloc[i]['link']
    print (moviename, '^^^^^', name)
    link1 = 'http://www.metacritic.com/movie/'
    link2 = '/critic-reviews'
    link = link1 + str(name) + link2

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
            positive = soup.find('div', class_='chart positive')
            positive = positive.find('div', class_='count fr').text.strip()
            mixed = soup.find('div', class_='chart mixed')
            mixed = mixed.find('div', class_='count fr').text.strip()
            negative = soup.find('div', class_='chart negative')
            negative = negative.find('div', class_='count fr').text.strip()
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
                source_link = 'http://www.metacritic.com' + each.find('span', class_='source').a['href']
            except:
                source_link = ''
            try:
                author = each.find('span', class_='author').text.strip()
            except:
                author = ''
            try:
                author_link = 'http://www.metacritic.com' + each.find('span', class_='author').a['href']
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

new_add = pd.DataFrame(output_list, columns=['rank', 'moviename', 'meta_movie_name', 'release_date', 'total_score',
                                   'num_crit', 'positive', 'mixed', 'negative', 'iscore', 'source', 'source_link', 'author', 'author_link', 'date', 'summary'])

df_right.drop(['moviename_y', 'link'], axis=1, inplace=True)
df_out = df_right.append(new_add, ignore_index = True)
df_out.to_csv('mc2_' +thisyear+'.csv')
