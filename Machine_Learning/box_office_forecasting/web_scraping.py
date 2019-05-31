import requests
from bs4 import BeautifulSoup
import csv
import time
import re

#Extract movie info from BoxOfficeMojo
def get_movie(movie_list):
    output_list = []
    for movie in movie_list:
        try:
            rank = movie.contents[0].text
            print(rank)
            name = movie.contents[1].text
            name_link = 'http://www.BoxOfficeMojo.com/' + movie.contents[1].b.font.a['href']
            total_gross = movie.contents[3].text.replace(',','').replace('$','')
            total_thea = movie.contents[4].text.replace(',','')
            open_gross = movie.contents[5].text.replace(',','').replace('$','')
            open_thea = movie.contents[6].text.replace(',','')
            open_date = movie.contents[7].text
            close_date = movie.contents[8].text
            studio = movie.contents[2].text

            details = get_details(name_link)
            budget = details[0]
            genre = details[2]
            runtime = details[3]
            MPAArating = details[4]
            Director_list = details[5]
            Director_links = details[6]
            Writer_list = details[7]
            Writer_links = details[8]
            Actor_list = details[9]
            Actor_links = details[10]
            Producer_list = details[11]
            Producer_links = details[12]
            Cinematographer_list = details[13]
            Cinematographer_links = details[14]
            Composer_list = details[15]
            Composer_links = details[16]
            output_list.append([rank, name, name_link, total_gross, total_thea, open_gross,
open_thea, open_date, close_date, budget, studio, genre, runtime, MPAArating, Director_list,
Director_links, Writer_list, Writer_links, Actor_list, Actor_links, Producer_list, Producer_links,
])
