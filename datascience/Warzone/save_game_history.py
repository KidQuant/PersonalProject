import requests
import json
import pandas as pd
import pickle
from datetime import datetime
import os
import urllib.request


gamerTags = pd.read_csv('GamerTags.csv')
gamerTags

data = None

def GetGameHistory(battlenet):

    import requests
    global data

    url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/{}/battle/".format(battlenet)

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

    df = df[df['Mode'] != 'br_dmz_plunquad']
    df = df.reset_index().drop(columns = ['index'])

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

    return df

data['errors']

df = GetGameHistory(gamerTags['BattleNet'][2])

def SaveGameHistory(user, df):

    with open('{}.pickle'.format(user), 'rb') as f:
        print('Collecting old matches for: {}'.format(user))
        old = pickle.load(f)

    new = pd.concat([df, old], ignore_index=False)
    new.drop_duplicates(subset = 'MatchID', inplace=True)
    new  = new.reset_index().drop(columns=['index'])

    with open('{}.pickle'.format(user), 'wb') as f:
        print('Storing new matches for: {}'.format(user))
        pickle.dump(new, f)

    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y %H%H%S")

    savePath = 'Game History/' + str(user)

    if not os.path.exists('{}'.format(savePath)):
        print('Creating Directory for {}'.format(user))
        os.mkdir('{}'.format(savePath))

    df.to_csv("{}/{}{}.csv".format(savePath, user, date_time))

SaveGameHistory(gamerTags['User'][2], df)
