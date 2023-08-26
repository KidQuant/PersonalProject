import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import os
import json
import time
import pyopenfec as api
from copy import deepcopy
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
logging.getLogger("requests").setLevel(logging.ERROR) # silencing requests logging

# Logging for this notebook
logger = logging.getLogger()
logger.setLevel(logging.INFO) # set this to whatever you'd like
import locale
locale.setlocale(locale.LC_ALL, '')

BASE_URL = 'http://api.open.fec.gov/v1'

API_KEY = open('key.txt','r').read().strip()
%env OPENFEC_API_KEY=bQhsk7IYSSpvB05Yz5ZgqDd09CzwkxEqPmekwAZa
promise_keepers = [c for c in api.Committee.search('Keep the Promise')]
