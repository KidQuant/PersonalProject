import pandas as pd
import json
import time
import csv
import requests

#define the year to extract data
thisyear = '2017'

#import film name and rank from BoxOfficeMojo
movie = pd.read_csv('box' + thisyear +'2.csv')
name = movie['name']
rank = movie['rank']

# create a csv to store IMDB data
movie_desc = []
movie_desc.append(['RankinBoxOffice','TitleinBoxOffice','Title', 'Year', 'imdbID', 'imdbRating', 'imdbVotes', 'Type', 'Website', 'Writer', 'Runtime',
                  'Response', 'Released', 'Ratings', 'Rated', 'Production', 'Poster', 'Plot', 'Metascore', 'Language', 'Genre',
                   'Director', 'DVD', 'Country', 'BoxOffice', 'Awards', 'Actors'])
with open('IMDB' + thisyear +'.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(movie_desc)

for i in range(0, len(name)):
    RankinBoxOffice = rank[i]
    TitleinBoxOffice = name[i]
    m = TitleinBoxOffice.replace(' (2017)','').replace(' ', '+')
    link = 'http://www.omdbapi.com/?t=' + m + '&apikey=e30d2be'
    r = requests.get(link)
    movie_json = json.loads(r.text)
    try:
        Title = movie_json['Title']
        Year = movie_json['Year']
        imdbID = movie_json['imdbID']
        imdbRating = movie_json['imdbRating']
        imdbVotes = movie_json['imdbVotes']
        Type = movie_json['Type']
        try:
            Website = movie_json['Website']
        except:
            Websit = ''
        Writer = movie_json['Writer'].replace(',','|')
        Runtime = movie_json['Runtime']
        Response = movie_json['Response']
        Released = movie_json['Released']
        Ratings = str(movie_json['Ratings']).replace(',','|')
        Rated =movie_json['Rated']
        try:
            Production = movie_json['Production']
        except:
            Production = ''
        Poster = movie_json['Poster']
        Plot = movie_json['Plot']
        Metascore = movie_json['Metascore']
        Language = movie_json['Language']
        Genre = movie_json['Genre'].replace(',','|')
        Director = movie_json['Director'].replace(',','|')
        try:
            DVD = movie_json['DVD']
        except:
            DVD = ''
        Country = movie_json['Country']
        try:
            BoxOffice = movie_json['BoxOffice']
        except:
            BoxOffice = ''
        Awards = movie_json['Awards']
        Actors = movie_json['Actors'].replace(',','|')
        movie_desc = [RankinBoxOffice, TitleinBoxOffice, Title, Year, imdbID, imdbRating, imdbVotes, Type, Website, Writer, Runtime,
                      Response, Released, Ratings, Rated, Production, Poster, Plot, Metascore, Language, Genre, Director, DVD, Country,
                     BoxOffice, Awards, Actors]
        print (TitleinBoxOffice)
    except:
        error = movie_json['Error']
        movie_desc = [RankinBoxOffice, TitleinBoxOffice, 'error']
        print ('Error @@@@@', TitleinBoxOffice)

    with open('IMDB' + thisyear +'.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow(movie_desc)

#Printing out incorrect movie matches

thisyear = '2017'
df = pd.read_csv('IMDB' + thisyear +'.csv')

df_not_match = df[~(df['TitleinBoxOffice'].str.lower() == df['Title'].str.lower())]

df_nomatch_noyear = df_not_match[~df_not_match['TitleinBoxOffice'].str.contains('\(' + thisyear + '\)')]

df_nomatch_year = df_not_match[df_not_match['TitleinBoxOffice'].str.contains('\(' + thisyear + '\)')]
df_nomatch_year = df_nomatch_year[df_nomatch_year['Title'] == 'error']

df_out = df_nomatch_noyear.append(df_nomatch_year)
df_out.to_csv('error' + thisyear + '.csv')
