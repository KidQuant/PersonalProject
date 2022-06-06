import requests
import json
import numpy as np
from datetime import datetime
import pandas as pd
import time

url = "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/battle/fullMatch/wz/1769968560950490708/it"

payload = {}
headers = {

}

response = requests.request("GET", url, headers=headers, data=payload)

# type(response.text)

data = json.loads(response.text)



players = data['data']['allPlayers']

index = 0
for i in players:

    if 'kdRatio' not in i['playerStats'].keys():
        print('{} kdRatio not in key of Dictionary'.format(index))
        del players[index]

    index += 1

if players[26]['playerStats']['kdRatio']:
    print(False)

for i in range(len(players)):
    print(i, players[i]['player']['username'])

    if 'Quants' in players[i]['player']['username']:
        print(players[i]['player']['username'])


players[6]['player']

np.average([x['playerStats']['kdRatio'] for x in players])

[x['playerStats']['kdRatio'] for x in players if]


lobby_players = response.json()['data']['allPlayers']
lobby_players_df = pd.DataFrame.from_records(lobby_players)
lobby_players_df.info()
lobby_players_df['playerStats']
lobby_players_df = pd.DataFrame.from_records(lobby_players_df['playerStats'])
lobby_players_df
lobby_players_df.info()
lobby_players_df.describe()


kds = []
lobby_players_full = []
team = ""
teamPlacement = ""
team_stats = {}
for player in lobby_players:
    time.sleep(0.2)
    if player['player']['uno'] in player.values():
        team = player['player']['team']
        team_placement = player['playerStats']['teamPlacement']
        team_stats[player['player']['username']] = [player['playerStats']['kills']]
    resp = requests.get('https://www.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/' + str(player['player']['uno']) + '/profile/type/warzone', headers=headers)
#    try resp.json()['data'].get('message', ) == "Not permitted: not allowed":
#        kds.append('NA')
#    catch:
    kds.append(resp.json().get('data', {}).get('lifetime', {}).get('mode', {}).get('br', {}).get('properties', {}).get('kdRatio'))
    lobby_players_full.append(resp.json()['data'])
kds

test = requests.get('https://www.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/3486743531844030789/profile/type/warzone')
test.json()