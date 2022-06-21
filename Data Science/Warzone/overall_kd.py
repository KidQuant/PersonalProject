import pickle
from selenium import webdriver
import json
import os

PATH = 'C:\Program Files (x86)\chromedriver.exe'

user = 'Quants'

with open('User History\{}.pickle'.format(user), 'rb') as f:
        print('Collecting old matches for: {}'.format(user))
        df = pickle.load(f)
        oldMatches = df['MatchID'].tolist()
        print(df.head())

oldMatches

endpoint = "https://api.tracker.gg/api/v1/warzone/matches/{}".format(oldMatches[0])

driver = webdriver.Chrome(PATH)
driver.get(endpoint)

body = driver.find_element_by_xpath("/html/body").text

data = json.loads(body)

driver.quit()

data['data']['attributes']['kdHistogram']

hist = []

for i in oldMatches:
        


