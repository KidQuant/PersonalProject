import requests
import urllib.request
import json
import datetime
import time

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,}

endpoint = "https://api.tracker.gg/api/v1/warzone/matches/1734752448278367972"
request = urllib.request.Request(endpoint, None, headers)
response = urllib.request.urlopen(request)

data = response.read()
jsonData = data.decode('utf8').replace("''", '"')

data = json.loads(jsonData)

data['data']['segments']

timestamp = data['data']['metadata']['timestamp']
dateTime = datetime.datetime.fromtimestamp(timestamp/1000)
date = dateTime.strftime("%m-%d-%Y")
time = dateTime.strftime("%H:%M:%S")

list(data['data']['attributes']['avgKd'].values())[0]

import requests
import json

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

data['matches'][1]
