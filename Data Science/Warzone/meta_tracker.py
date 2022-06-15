import urllib.request
import requests
import json
import pandas as pd
import pickle


import requests


match_id = "447620116446864960"

url = "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/battle/fullMatch/wz/{}/it".format(match_id)

headers = {
	"X-RapidAPI-Key": "e6c6bbe19amshdfe963bc74bf7dap1d5654jsn50ad5279af3c",
	"X-RapidAPI-Host": "call-of-duty-modern-warfare.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)

data['matches'][0]['player']