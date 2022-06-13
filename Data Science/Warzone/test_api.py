from bs4 import BeautifulSoup
import requests

url = 'https://api.tracker.gg/api/v2/warzone/matches/2346808456641629496'

response = requests.get(url)