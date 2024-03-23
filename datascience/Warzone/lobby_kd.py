
import requests
import urllib.parse
import random
import os
import pandas as pd
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import json
from selenium import webdriver
%matplotlib inline


# sso_token = "MTczNzE4NDQ4NDY2MzE4NDgxNTk6MTY1NTQ5ODUwNjExNjo4ODZmMmNjNTUwNzFlY2U4OTgwMTEzYzllOTMxZDhjMQ"
# cookies={"ACT_SSO_COOKIE": sso_token}

# resp_profile = requests.get('https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/xbl/gamer/coltie119/matches/wz/start/0/end/0/details', cookies=cookies)
# uno = resp_profile.json()['data']['matches'][0]['player']['uno']


s = requests.Session()
s.get('https://profile.callofduty.com/cod/login')

data = {'username': 'andre@kidquant.com', 
        'password': 'Dre_kamaza93', 
        'remember_me': 'true', 
        '_csrf': s.cookies['XSRF-TOKEN']}

s.post('https://profile.callofduty.com/do_login?new_SiteId=cod', params=data)

match_id = "6523302528087950146"

url = "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/battle/fullMatch/wz/{}/it".format(match_id)

payload = {}
headers = {

}

response = requests.request("GET", url, headers=headers, data=payload)



lobby_players = response.json()['data']['allPlayers']
lobby_players_df = pd.DataFrame.from_records(lobby_players)
lobby_players_df.info()

for i in range(len(lobby_players)):
        username = lobby_players[i]['player']['username']
        uno = lobby_players[i]['player']['uno']
        print('{} : {}'.format(username, uno))

lobby_players_df['playerStats']

lobby_players_df = pd.DataFrame.from_records(lobby_players_df['playerStats'])
lobby_players_df

lobby_players_df.info()


headers = {
	"X-RapidAPI-Host": "call-of-duty-modern-warfare.p.rapidapi.com",
	"X-RapidAPI-Key": "e6c6bbe19amshdfe963bc74bf7dap1d5654jsn50ad5279af3c"
}



for i in range(len(lobby_players)):
        time.sleep(2)
        uno = lobby_players[i]['player']['uno']
        user = lobby_players[i]['player']['username']
        url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/{}/uno".format(uno)
        response = requests.request("GET", url, headers=headers)



        if 'br' in response.json().keys():
                kd = response.json()['br']['kdRatio'] 
                print("{}: {} | {}".format(user, kd, uno))

        else:
                print("{}: NA Player | {}".format(user, uno))


        # print(lobby_players[i]['player']['username'] + ': ' + lobby_players[i]['player']['uno'] )
import requests


endpoint = "https://api.tracker.gg/api/v1/warzone/matches/11435916617093634673"
r = requests.get(endpoint)
data = r.json()["data"]

from selenium import webdriver
import json

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://api.tracker.gg/api/v1/warzone/matches/11435916617093634673")
test = driver.find_element_by_xpath("/html/body").text
json.loads(test)


driver.quit()