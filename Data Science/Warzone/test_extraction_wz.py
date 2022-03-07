import requests
import json
import pandas as pd
import pickle
from datetime import datetime
import pandas as pd
import os

gamerTags = pd.read_csv('GamerTags.csv')
gamerTags.head()

user = gamerTags['User'][2]
battleNet = gamerTags['BattleNet'][2]

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

df = df[df['Mode'] != 'br_dmz_plunquad']
df = df.reset_index().drop(columns= ['index'])

import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,}


# endpoint = "https://api.tracker.gg/api/v1/warzone/matches/10508390693456844744"
# request = urllib.request.Request(endpoint, None, headers)
# response = urllib.request.urlopen(request)
# data = response.read()
# jsonData = data.decode('utf8')
# data = json.loads(jsonData)
# avg = list(data['data']['attributes']['avgKd'].values())[0]

avgKD = []
matchDate = []
matchTime = []

for i in df['MatchID']:
    endpoint = "https://api.tracker.gg/api/v1/warzone/matches/{}".format(i)
    request = urllib.request.Request(endpoint, None, headers)
    response = urllib.request.urlopen(request)

    data = response.read()
    jsonData = data.decode('utf8')

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

new = df

with open('{}.pickle'.format(user), 'rb') as f:
    print('Collecting old matches for: {}'.format(user))
    old = pickle.load(f)

new = pd.concat([df, old], ignore_index=False)
new.drop_duplicates(subset = 'MatchID', inplace=True)
new = new.reset_index().drop(columns=['index'])

with open('{}.pickle'.format(user), 'wb') as f:
    print('Storing new matches for: {}'.format(user))
    pickle.dump(new, f)

now = datetime.now()
date_time =  now.strftime("%m-%d-%Y %H%H%S")

savePath = 'Game History/' + str(user)

if not os.path.exists('{}'.format(savePath)):
    os.mkdir('{}'.format(savePath))


df.to_csv("{}/{}{}.csv".format(savePath, user, date_time))
