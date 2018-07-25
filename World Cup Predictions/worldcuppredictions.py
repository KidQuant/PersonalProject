import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from plotly.offline import iplot, init_notebook_mode
from geopy.geocoders import Nominatim
import plotly.plotly as py

FIFA18 = pd.read_csv('/Users/Dre/Documents/GitHub/PersonalProject/World Cup Predictions/fifa-18-demo-player-dataset/CompleteDataset.csv', low_memory = False)
