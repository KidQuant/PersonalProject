import requests
from bs4 import BeautifulSoup
import csv
import time
import re

# Extract movie info from BoxOfficeMojo
def get_movie(movie_list):
    output_list = []
    for movie in movie_list:
        try:
            rank = movie.contents[0].text
            print (rank)
            name = movie.contents[1].text
            name_link = 'http://www.boxofficemojo.com/' + movie.contents[1].b.font.a['href']
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
            output_list.append([rank, name, name_link, total_gross, total_thea, open_gross, open_thea, open_date, close_date, budget, studio, genre, runtime, MPAArating, Director_list, Director_links, Writer_list, Writer_links, Actor_list, Actor_links, Producer_list, Producer_links, Cinematographer_list, Cinematographer_links, Composer_list, Composer_links])
        except Exception as ex:
            print(ex)
    return output_list

# Enter each page of the movie to get detailed information

def get_details(name_link):
    try:
        budget = ""
        distributor =""
        genre = ""
        runtime = ""
        MPAArating = ""
        Director_list = ""
        Director_links = ""
        Writer_list = ""
        Writer_links = ""
        Actor_list = ""
        Actor_links = ""
        Producer_list = ""
        Producer_links = ""
        Cinematographer_list = ""
        Cinematographer_links = ""
        Composer_list = ""
        Composer_links = ""
        r = requests.get(name_link, headers=headers)
        html = r.text
        budget = re.findall('<td valign="top">Production Budget: <b>(.*?)</b></td>', html)[0]
        distributor = re.findall(r'<td valign="top">Distributor: <b><a href=".*?">(.*?)</a></b></td>', html)[0]
        genre = re.findall('<td valign="top">Genre: <b>(.*?)</b></td>', html)[0]
        runtime = re.findall('<td valign="top">Runtime: <b>(.*?)</b></td>', html)[0]
        MPAArating = re.findall('<td valign="top">MPAA Rating: <b>(.*?)</b></td>', html)[0]
        soup = BeautifulSoup(html, 'lxml')
        players = soup.find_all('div', class_="mp_box_content")[2].table
        for eachplay in players.find_all('tr'):
            title = eachplay.td.text.replace(":","")
            if title == "Directors" or title == "Director":
                td2 = eachplay.contents[1]
                a_list = td2.find_all('a')
                for i in range(0,len(a_list)):
                    player = a_list[i].text
                    player_link = a_list[i]['href']
                    Director_list = Director_list + player +" | "
                    Director_links = Director_links + player_link +" | "
            elif title == "Writers" or title == "Writer":
                td2 = eachplay.contents[1]
                a_list = td2.find_all('a')
                for i in range(0,len(a_list)):
                    player = a_list[i].text
                    player_link = a_list[i]['href']
                    Writer_list = Writer_list + player +" | "
                    Writer_links = Writer_links + player_link +" | "
            elif title == "Actors" or title == "Actor":
                td2 = eachplay.contents[1]
                a_list = td2.find_all('a')
                for i in range(0,len(a_list)):
                    player = a_list[i].text
                    player_link = a_list[i]['href']
                    Actor_list = Actor_list + player +" | "
                    Actor_links = Actor_links + player_link +" | "
            elif title == "Producers" or title == "Producer":
                td2 = eachplay.contents[1]
                a_list = td2.find_all('a')
                for i in range(0,len(a_list)):
                    player = a_list[i].text
                    player_link = a_list[i]['href']
                    Producer_list = Producer_list + player +" | "
                    Producer_links = Producer_links + player_link +" | "
            elif title == "Cinematographers" or title == "Cinematographer":
                td2 = eachplay.contents[1]
                a_list = td2.find_all('a')
                for i in range(0,len(a_list)):
                    player = a_list[i].text
                    player_link = a_list[i]['href']
                    Cinematographer_list = Cinematographer_list + player +" | "
                    Cinematographer_links = Cinematographer_links + player_link +" | "
            elif title == "Composers" or title == "Composer":
                td2 = eachplay.contents[1]
                a_list = td2.find_all('a')
                for i in range(0,len(a_list)):
                    player = a_list[i].text
                    player_link = a_list[i]['href']
                    Composer_list = Composer_list + player +" | "
                    Composer_links = Composer_links + player_link +" | "
    except Exception as ex:
        print (ex)
    return_list = [budget, distributor, genre, runtime, MPAArating, Director_list, Director_links, Writer_list, Writer_links, Actor_list, Actor_links, Producer_list, Producer_links, Cinematographer_list, Cinematographer_links, Composer_list, Composer_links]
    return return_list

# define the year
year = '2017'
# define the link
link1 = 'http://www.boxofficemojo.com/yearly/chart/?page='
link2 = '&view=widedate&view2=domestic&yr=' + year +'&p=.htm'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

output_list = []
output_list.append(['rank', 'name', 'name_link', 'total_gross', 'total_thea', 'open_gross', 'open_thea', 'open_date', 'close_date', 'budget', 'studio', 'genre', 'runtime', 'MPAArating', 'Director_list', 'Director_links', 'Writer_list', 'Writer_links', 'Actor_list', 'Actor_links', 'Producer_list', 'Producer_links', 'Cinematographer_list', 'Cinematographer_links', 'Composer_list', 'Composer_links'])
with open('box' + year +'2.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerows(output_list)

# get the info from BoxOfficeMojo
for i in range(1,3):
    print (i)
    output_list = []
    link = link1 + str(i) + link2
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    movie_list1 = soup.find_all('tr', attrs={"bgcolor": "#ffffff"})
    movie_list2 = soup.find_all('tr', attrs={"bgcolor": "#f4f4ff"})

    output_list = output_list + get_movie(movie_list1)
    output_list = output_list + get_movie(movie_list2)
    with open('box' + year +'2.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(output_list)
    time.sleep(3)
