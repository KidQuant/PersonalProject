import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from plotly.offline import iplot, init_notebook_mode
from geopy.geocoders import Nominatim
import plotly.plotly as py

FIFA18 = pd.read_csv('/Users/Dre/Documents/GitHub/PersonalProject/World Cup Predictions/fifa-18-demo-player-dataset/CompleteDataset.csv', low_memory = False)
FIFA18.columns

interesting_columns = [
    'Name',
    'Age',
    'Nationality',
    'Overall',
    'Potential',
    'Club',
    'Value',
    'Wage',
    'Preferred Positions']

FIFA18 = pd.DataFrame(FIFA18, columns = interesting_columns)

FIFA18.info()

def str2number(amount):
    if amount[-1] == 'M':
        return float(amount[1:-1]) * 1000000
    elif amount[-1] == 'K':
        return float(amount[1:-1]) * 1000
    else:
        return float(amount[1:])

FIFA18['ValueNum'] = FIFA18['Value'].apply(lambda x: str2number(x))
FIFA18['WageNum'] = FIFA18['Wage'].apply(lambda x: str2number(x))

FIFA18['Position'] = FIFA18['Preferred Positions'].str.split().str[0]

plt.figure(figsize=(16,8))
sns.set_style('whitegrid')
plt.title('Grouping players by Age', fontsize=30, fontweight='bold', y=1.05)
plt.xlabel('Number of player', fontsize=25)
plt.ylabel('Player age', fontsize=25)
sns.countplot(x='Age', data=FIFA18, palette='hls')
plt.show()
