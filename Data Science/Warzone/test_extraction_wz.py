import requests
import json
import pandas as pd
import pickle
from datetime import datetime
import pandas as pd

gamerTags = pd.read_csv('GamerTags.csv')
gamerTags.head()

user = gamerTags['User'][1]
battleNet = gamerTags['BattleNet'][1]

url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/{}/battle/".format(battleNet)

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers = {
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
    'x-rapidapi-key': "e6c6bbe19amshdfe963bc74bf7dap1d5654jsn50ad5279af3c",
    'User-Agent':user_agent
    }


response = requests.request("GET", url, headers=headers)

print(response.text)

data = json.loads(response.text)

matchID = []
gameMode = []
kills = []
deaths = []
kdRatio = []


for i in data['matches']:
    matchID.append(i['matchID'])
    gameMode.append(i['mode'])
    kills.append(i['playerStats']['kills'])
    deaths.append(i['playerStats']['deaths'])
    kdRatio.append(i['playerStats']['kdRatio'])

df = pd.DataFrame()

df['MatchID'] = matchID
df['Mode'] = gameMode
df['Kills'] = kills
df['Deaths'] = deaths
df['KDRatio'] = kdRatio
df.head()

import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,}

avgKD = []
matchDate = []
matchTime = []

for i in df['MatchID']:
    endpoint = "https://api.tracker.gg/api/v1/warzone/matches/{}".format(i)
    request = urllib.request.Request(endpoint, None, headers)
    response = urllib.request.urlopen(request)

    data = response.read()
    jsonData = data.decode('utf8').replace("''", '"')

    data = json.loads(jsonData)

    avg = list(data['data']['attributes']['avgKd'].values())[0]

    timestamp = data['data']['metadata']['timestamp']
    dateTime = datetime.fromtimestamp(timestamp/1000)
    date = dateTime.strftime("%m-%d-%Y")
    time = dateTime.strftime("%H:%M:%S")

    print('Match ID: {} | Lobby KD: {}'.format(i, avg))

    matchDate.append(date)
    matchTime.append(time)
    avgKD.append(avg)

df['LobbyKD'] = avgKD
df['Date'] = matchDate
df['Time'] = matchTime

with open('{}.pickle'.format(user), 'rb') as f:
    old = pickle.load(f)


with open('{}.pickle'.format(user), 'wb') as f:
    pickle.dump(df, f)

now = datetime.now()
date_time =  now.strftime("%m-%d-%Y %H%H%S")

df.to_csv("{}{}.csv".format(gamerTags['User'][1],date_time))
