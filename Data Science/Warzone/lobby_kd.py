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
%matplotlib inline

sso_token = "MTczNzE4NDQ4NDY2MzE4NDgxNTk6MTY1NTQ5ODUwNjExNjo4ODZmMmNjNTUwNzFlY2U4OTgwMTEzYzllOTMxZDhjMQ"
cookies={"ACT_SSO_COOKIE": sso_token}

resp_profile = requests.get('https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/xbl/gamer/coltie119/matches/wz/start/0/end/0/details', cookies=cookies)
uno = resp_profile.json()['data']['matches'][0]['player']['uno']


s = requests.Session()
s.get('https://profile.callofduty.com/cod/login')

data = {'username': 'andre@kidquant.com', 
        'password': 'Dre_kamaza93', 
        'remember_me': 'true', 
        '_csrf': s.cookies['XSRF-TOKEN']}

s.post('https://profile.callofduty.com/do_login?new_SiteId=cod', params=data)

match_id = "11435916617093634673"

url = "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/battle/fullMatch/wz/{}/it".format(match_id)

payload = {}
headers = {

}

response = requests.request("GET", url, headers=headers, data=payload)



lobby_players = response.json()['data']['allPlayers']
lobby_players_df = pd.DataFrame.from_records(lobby_players)
lobby_players_df.info()

lobby_players_df['playerStats']

lobby_players_df = pd.DataFrame.from_records(lobby_players_df['playerStats'])
lobby_players_df

lobby_players_df.info()

playerurl = 'https://www.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/' + str(lobby_players[43]['player']['uno']) + '/profile/type/warzone'

player = requests.request("GET", playerurl, cookies=cookies)

player.json()