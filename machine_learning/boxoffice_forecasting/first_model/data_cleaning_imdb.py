import pandas as pd
import numpy as np
import requests
import json
import time
from bs4 import BeautifulSoup
import csv

thisyear = '2017'
box = pd.read_csv('box' + thisyear + '2.csv')
imdb = pd.read_csv('IMDB' + thisyear + '.csv')
error = pd.read_csv('error' + thisyear + '.csv')

box_imdb = pd.merge(box, imdb,  how='inner', left_on=['rank'], right_on = ['RankinBoxOffice'])
all_wide = pd.merge(box_imdb, error,  how='left', left_on=['rank'], right_on = ['RankinBoxOffice'])

for i in range(0, len(all_wide)):
    if pd.notnull(all_wide['imdbID_x'])[i]:
        m = all_wide.iloc[i]['imdbID_x']
        link = 'http://www.omdbapi.com/?i=' + m + '&apikey=e30d2be'
        print (link)
        r = requests.get(link)
        movie_json = json.loads(r.text)

        all_wide.at[i, 'Title'] = movie_json['Title']
        all_wide.at[i, 'Year'] = movie_json['Year']
        all_wide.at[i, 'imdbID'] = movie_json['imdbID']
        all_wide.at[i, 'imdbRating'] = movie_json['imdbRating']
        all_wide.at[i, 'imdbVotes'] = movie_json['imdbVotes']
        all_wide.at[i, 'Type'] = movie_json['Type']
        try:
            all_wide.at[i, 'Website'] = movie_json['Website']
        except:
            all_wide.at[i, 'Website'] = ''
        all_wide.at[i, 'Writer'] = movie_json['Writer'].replace(',','|')
        all_wide.at[i, 'Runtime'] = movie_json['Runtime']
        all_wide.at[i, 'Response'] = movie_json['Response']
        all_wide.at[i, 'Released'] = movie_json['Released']
        all_wide.at[i, 'Ratings'] = str(movie_json['Ratings']).replace(',','|')
        all_wide.at[i, 'Rated'] =movie_json['Rated']
        try:
             all_wide.at[i, 'Production'] = movie_json['Production']
        except:
             all_wide.at[i, 'Production'] = ''
        all_wide.at[i, 'Poster'] = movie_json['Poster']
        all_wide.at[i, 'Plot'] = movie_json['Plot']
        try:
            all_wide.at[i, 'Metascore'] = movie_json['Metascore']
        except:
            pass
        all_wide.at[i, 'Language'] = movie_json['Language']
        all_wide.at[i, 'Genre'] = movie_json['Genre'].replace(',','|')
        all_wide.at[i, 'Director'] = movie_json['Director'].replace(',','|')
        try:
            all_wide.at[i, 'DVD'] = movie_json['DVD']
        except:
            all_wide.at[i, 'DVD'] = ''
        all_wide.at[i, 'Country'] = movie_json['Country']
        try:
            all_wide.at[i, 'BoxOffice'] = movie_json['BoxOffice']
        except:
            all_wide.at[i, 'BoxOffice'] = ''
        all_wide.at[i, 'Awards'] = movie_json['Awards']
        all_wide.at[i, 'Actors'] = movie_json['Actors'].replace(',','|')
all_wide.drop(['RankinBoxOffice_x', 'TitleinBoxOffice_x','RankinBoxOffice_y','TitleinBoxOffice_y', 'imdbID_y'], axis=1, inplace=True)
all_wide.to_csv('all_wide_'+ thisyear +'.csv')
