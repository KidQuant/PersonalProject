import pickle
from selenium import webdriver
import json
import os
from datetime import datetime
import pandas as pd


PATH = 'C:\Program Files (x86)\chromedriver.exe'

gamerTags = pd.read_csv('GamerTags.csv')
user = gamerTags['User'][2]

with open('User History\{}.pickle'.format(user), 'rb') as f:
    print('Collecting old matches for: {}'.format(user))
    df = pickle.load(f)

today = datetime.today().strftime('%m-%d-%Y')

brDF = df[~df['Mode'].str.contains('rebirth')]
dateDF = brDF[brDF['Date'] == today]

# endpoint = 'https://api.tracker.gg/api/v1/warzone/matches/battlenet/diazbiffle%231415?/type=wz&next=null'
# driver = webdriver.Chrome(PATH)
# driver.get(endpoint)

# body = driver.find_element_by_xpath("/html/body").text


hist = []

for i in dateDF['MatchID']:

        print(i)

        endpoint = "https://api.tracker.gg/api/v1/warzone/matches/{}".format(i)
        driver = webdriver.Chrome(PATH)
        driver.get(endpoint)

        body = driver.find_element_by_xpath("/html/body").text

        data = json.loads(body)

        driver.quit()

        histogram = data['data']['attributes']['kdHistogram']

        for obs in histogram:
                print(obs)

                hist.append(obs)

hist = []
for user in gamerTags['User']:
    with open('User History\{}.pickle'.format(user), 'rb') as f:
        print('Colling old matches for: {}'.format(user))
        df = pickle.load(f)

    brDF = df[~df['Mode'].str.contains('rebirth')]
    dateDF = brDF[brDF['Date'] == today]


    for i in dateDF['MatchID']:

        print(i)
        print('')

        endpoint = "https://api.tracker.gg/api/v1/warzone/matches/{}".format(i)
        driver = webdriver.Chrome(PATH)
        driver.get(endpoint)

        body = driver.find_element_by_xpath("/html/body").text

        match = json.loads(body)

        driver.quit()

        histogram = match['data']['attributes']['kdHistogram']

        for data in histogram:
            print(data)

            hist.append(data)




