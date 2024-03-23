import pandas as pd
import numpy as np

from dateutil.parser import parse
from datetime import datetime
import dateutil.parser

import matplotlib.pyplot as plt
%matplotlib inline

import seaborn as sns

import glob
import os
import zipfile

import timeit
import requests

from bs4 import BeautifulSoup
import re
import urllib
from bs4 import BeautifulSoup, element

import nltk

import statsmodels.api as sm
import statsmodels.formula.api as smf
import patsy

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

import statsmodels.api as sm

##########################################
# December
##########################################

# bring in vg chart data from url
url = 'http://www.vgchartz.com/preorders/43436/USA/'

response = requests.get(url)

tables = pd.read_html(url)

# convert list object to a dataframe
dec_df = pd.DataFrame(tables[0])
