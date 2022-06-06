import requests
import random
import os

s = requests.Session()
s.get('https://profile.callofduty.com/cod/login')
data = {'username': 'andre@kidquant.com', 
        'password': 'Dre_kamaza93', 
        'remember_me': 'true', 
        '_csrf': s.cookies['XSRF-TOKEN']}
s.post('https://profile.callofduty.com/do_login?new_SiteId=cod', params=data)


resp_profile = s.get('https://www.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/uno/17371844846631848159/profile/type/warzone')

resp_profile.json()