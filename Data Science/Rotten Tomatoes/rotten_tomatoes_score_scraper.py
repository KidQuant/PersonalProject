import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import requests
import waybackpy
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0'

#2018 scraper

def get_score(soup):
    critic = soup.find('span', {'class': "meter-value superPageFontColor"})
    audience = soup.find('div', {'class': "audience-score meter"}).find('span', {'class': "superPageFontColor"})
    return [critic.text, audience.text]

#2019-21 scraper
def getScore(soup):
    temp = soup.find_all('div', class_='mop-ratings-wrap__half')
    try:
        critic = temp[0].text.strip().replace('\n', '').split(' ')[0] #2020 scraper
        if len(temp) > 1:
            audience = temp[1].text.strip().replace('\n', '').split(' ')[0]
        else:
            audience = "Coming"
    except:
        scores = soup.find("score-board") #2021 scraper
        return [scores["tomatometerscore"], scores["audiencescore"]]
    return [critic, audience]

#get number of critic and audience reviews
def getNumReviews(soup):
    critic = soup.find_all("small", class_="mop-ratings-wrap__text--small")
    audience = soup.find_all("strong", class_="mop-ratings-wrap__text--small")
    if critic:
        critic = critic[0].text.replace("\n", '').strip()
    else:
        critic = soup.find_all("a", class_='scoreboard__link scoreboard__link--tomatometer')
        critic = critic[0].text
    if len(audience) > 1:
        audience = audience[1].text.replace("Verified Ratings: ", '')
    else:
        audience = soup.find_all("a", class_='scoreboard__link scoreboard__link--audience')
        if audience:
            audience = audience[0].text
        else:
            audience = "Coming"
    return [critic, audience]

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

#for 2019-21
def build(key, date1, date2):
    dates = pd.date_range(date1, date2).tolist()
    wayback = waybackpy.Url(movie_urls[key], user_agent)
    scores = []
    for date in dates:
        try:
            archived = wayback.near(year=date.year, month=date.month, day=date.day).archive_url
        except:
            print(date)
            continue
        page = requests.get(archived).text
        soup = BeautifulSoup(page, 'lxml')
        scores.append(getScore(soup) + getNumReviews(soup) + [date, key])
    return scores

#for 2017-18
def build2(key, date1, date2):
    dates = pd.date_range(date1, date2).tolist()
    wayback = waybackpy.Url(movie_urls[key], user_agent)
    scores = []
    for date in dates:
        try:
            archived = wayback.near(year=date.year, month=date.month, day=date.day).archive_url
        except:
            print(date)
            continue
        page = requests.get(archived).text
        soup = BeautifulSoup(page, 'lxml')
        scores.append(get_score(soup) + getNumReviews(soup) + [date, key])
    return scores

joker = build("Joker", '2019-09-03', '2020-09-03')
joker

captain = build("Captain Marvel", '2019-03-06', '2020-03-06')
captain

lion = build("Lion King", '2019-07-11', '2020-07-11')
lion

aladdin = build("Aladdin", '2019-05-23', '2020-05-23')
aladdin

shazam = build("Shazam!", '2019-03-24', '2020-03-24')
shazam

godzilla = build("Godzilla: King of the Monsters", '2019-05-31', '2020-05-31')
godzilla

arr = [captain, joker, lion, aladdin, shazam, godzilla]
dfs = []

for movie in arr:
    dfs.append(pd.DataFrame(movie, columns=["critic", "audience", "criticNum", "audienceNum", "date", "film"]))

pd.concat(dfs).to_csv('all_films_wayback_2019_reviews.csv', index=False)
