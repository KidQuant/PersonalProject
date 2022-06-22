import pickle
from selenium import webdriver
import json
import os

PATH = 'C:\Program Files (x86)\chromedriver.exe'

user = 'Diaz Biffle'

with open('User History\{}.pickle'.format(user), 'rb') as f:
    print('Collecting old matches for: {}'.format(user))
    df = pickle.load(f)


# endpoint = 'https://api.tracker.gg/api/v1/warzone/matches/battlenet/diazbiffle%231415?/type=wz&next=null'
# driver = webdriver.Chrome(PATH)
# driver.get(endpoint)

# body = driver.find_element_by_xpath("/html/body").text

df = df[df['Date'] == '06-20-2022']
oldMatches = df['MatchID'].tolist()


hist = []

for i in oldMatches:

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


