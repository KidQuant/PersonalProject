import requests
import time

#requirement
from bs4 import BeautifulSoup
from requests import TooManyRedirects
import re

def make_soup(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
    except TooManyRedirects:
        soup = ''
    return soup

#regex patterns
page_pat = re.compile(r'Page 1 of \d+')
review_pat = re.compile(r'<div class=\"the_review\" data-qa=\"review-text\">[;a-zA-Z\s,-.\'\/\?\[\]\":\']*</div>')
rating_pat = re.compile(r'Original Score:\s([A-Z](\+|-)?|\d(.\d)?(\/\d)?)')
fresh_pat = re.compile(r'small\s(fresh|rotten)\"')
critic_pat = re.compile(r'\/\"\>([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z\-]+)|([A-Z][a-zA-Z.]+\s[A-Z].?\s[A-Z][a-zA-Z]+)|([A-Z][a-zA-Z]+\s[A-Z]+\'[A-Z][a-zA-Z]+)')
publisher_pat = re.compile(r'\"subtle\">[a-zA-Z\s,.\(\)\'\-&;!\/\d+]+</em>')
date_pat = re.compile(r'[a-zA-Z]+\s\d+,\s\d+')

def get_critic_reviews_from_page(soup):
    reviews = list()
    rating = list()
    fresh = list()
    critic = list()
    top_critic = list()
    publisher = list()
    date = list()

    soup = str(soup)
    review_soup = soup.split('="review_table')[1].split('row review_table_row')
    review_soup.pop(0)

    for review in review_soup:
        match = re.findall(review_pat, str(review))
        if len(match) > 0:
            m = match[0]
            for iden in ['<div class="the_review" data-qa="review-text"> ','</div>']:
                m = m.replace(iden,'')
            reviews.append(m.strip('"'))
            # extract rating
            match = re.findall(rating_pat, str(review))
            if len(match) > 0:
                m = match[0][0]
                if '/1' in m:
                    sp_m = m.split('/')
                    if sp_m[-1] == '1':
                        sp_m[-1] = '10'
                    m = '/'.join(sp_m)
                rating.append(m)
            else:
                rating.append(None)
            # extract fresh indicator
            match = re.findall(fresh_pat, str(review))
            if len(match) > 0:
                fresh.append(match[0])
            else:
                fresh.append(None)
            # extract critic
            match = re.findall(critic_pat, str(review))
            if len(match) > 0:
                critic.append(''.join(match[0]))
            else:
                critic.append(None)
            # check if top critic
            if '> Top Critic<' in str(review):
                top_critic.append(1)
            else:
                top_critic.append(0)
            # extract publisher
            match = re.findall(publisher_pat, str(review))
            if len(match) > 0:
                m = match[0]
                m = m.replace('"subtle">', '')
                m = m.replace('</em>','')
                publisher.append(m)
            else:
                publisher.append(None)
            # extract date
            match = re.findall(date_pat, str(review))
            if len(match) > 0:
                date.append(match[0].strip('"'))
            else:
                date.append(None)

    return [reviews, rating, fresh, critic, top_critic, publisher, date]

def get_num_pages(soup):
    match = re.findall(page_pat,str(list(soup)))
    if len(match) > 0:
        match = match[0]
        match = match.split(' of ')[-1]
        return match
    else:
        return None

def get_critic_reviews(page):
    info = [[],[],[],[],[],[],[]]
    soup = make_soup(page + "reviews")
#     print(soup)
    pages = get_num_pages(soup)
#     print(pages)
    if pages is not None:
        for page_num in range(1,int(pages)+1):
            soup = make_soup(page + "reviews?page=" + str(page_num) + "&sort=")
            c_info = get_critic_reviews_from_page(soup)

            # accumulate review info
            for i in range(len(c_info)):
                info[i] = info[i] + c_info[i]

        c_info = dict()
        keys = ['reviews', 'rating', 'fresh', 'critic', 'top_critic', 'publisher', 'date']
        for k in range(len(keys)):
            c_info[keys[k]] = info[k]
    else:
        c_info = None
    return c_info


movie_urls = {'Wonder Woman 1984': 'https://www.rottentomatoes.com/m/wonder_woman_1984/',
              'Soul':'https://www.rottentomatoes.com/m/soul_2020/',
              'Mulan': 'https://www.rottentomatoes.com/m/mulan_2020/',
              'Birds of Prey': 'https://www.rottentomatoes.com/m/birds_of_prey_2020/',
              'Sonic': 'https://www.rottentomatoes.com/m/sonic_the_hedgehog_2020/'
             }

movie_urls["Captain Marvel"] = "https://www.rottentomatoes.com/m/captain_marvel/"
movie_urls["Lion King"] = "https://www.rottentomatoes.com/m/the_lion_king_2019/"
movie_urls["Aladdin"] = "https://www.rottentomatoes.com/m/aladdin/"
movie_urls["Joker"] = "https://www.rottentomatoes.com/m/joker_2019/"
movie_urls["Shazam!"] = "https://www.rottentomatoes.com/m/shazam/"
movie_urls["Godzilla: King of the Monsters"] = "https://www.rottentomatoes.com/m/godzilla_king_of_the_monsters_2019/"

movie_urls['Tenet'] = 'https://www.rottentomatoes.com/m/tenet/'
movie_urls['Scoob'] = 'https://www.rottentomatoes.com/m/scoob/'
movie_urls['The Marksman'] = 'https://www.rottentomatoes.com/m/the_marksman_2021/'
movie_urls['Artemis Fowl'] = 'https://www.rottentomatoes.com/m/artemis_fowl/'
movie_urls['Lovebirds'] = 'https://www.rottentomatoes.com/m/the_lovebirds_2020/'

movie_urls.keys()

import pandas as pd

dfs = []
for key in movie_urls.keys():
    temp = get_critic_reviews(movie_urls[key])
    df = pd.DataFrame.from_dict(temp)
    df['Film'] = key
    dfs.append(df)


all_films = pd.concat(dfs)
all_films

all_films['score'] = all_films['fresh'].apply(lambda x: 1 if x == 'fresh' else 0)
all_films

import numpy as np

def calculate_score(film, frame):
    df = frame[frame['Film'] == film]
    grouped_1 = df[['date', 'score']].groupby('date').agg([sum, 'count'])
    grouped_1.columns = grouped_1.columns.droplevel(0)
    return grouped_1.cumsum()['sum'] / grouped_1.cumsum()['count']

calculate_score('Wonder Woman 1984', all_films)
