import requests
import json
import pandas as pd
import pickle
from datetime import datetime

url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/icemanisaac%231815/battle/"

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers = {
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
    'x-rapidapi-key': "e6c6bbe19amshdfe963bc74bf7dap1d5654jsn50ad5279af3c",
    'User-Agent':user_agent
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

data = json.loads(response.text)
data['matches'][0]


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

with open('icemanisaac.pickle', 'rb') as f:
    df = pickle.load(f)

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


for i in df['MatchID']:
    endpoint = "https://api.tracker.gg/api/v1/warzone/matches/{}".format(i)
    request = urllib.request.Request(endpoint, None, headers)
    response = urllib.request.urlopen(request)

    data = response.read()
    jsonData = data.decode('utf8').replace("''", '"')

    data = json.loads(jsonData)

    avg = list(data['data']['attributes']['avgKd'].values())[0]
    print('Match ID: {} | Lobby KD: {}'.format(i, avg))

    avgKD.append(avg)

df['LobbyKD'] = avgKD

with open('icemanisaac.pickle', 'wb') as f:
    pickle.dump(df, f)

now = datetime.now()
date_time =  now.strftime("%m-%d-%Y %H%H%S")
type(date_time)
df.to_csv("Icemanissac{}.csv".format(date_time))
