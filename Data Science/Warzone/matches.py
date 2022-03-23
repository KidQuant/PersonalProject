import requests
import json

import pandas as pd
import pickle
from datetime import datetime

url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/doozy%252311186/battle/"

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers = {
    'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
    'x-rapidapi-key': "e6c6bbe19amshdfe963bc74bf7dap1d5654jsn50ad5279af3c",
    'User-Agent':user_agent
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
