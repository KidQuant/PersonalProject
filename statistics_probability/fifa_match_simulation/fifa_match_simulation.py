import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.ticker as plticker
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

world_cup = pd.read_csv('statistics_probability/fifa_match_simulation/World Cup 2018 Dataset.csv')
results = pd.read_csv('statistics_probability/fifa_match_simulation/results.csv')

world_cup.head()

results.head()

winner = []
for i in range (len(results['home_team'])):
    if results['home_score'][i] > results['away_score'][i]:
        winner.append(results['home_team'][i])
    elif results['home_score'][i < results ['away_score'][i]:
        winner.append(results['away_team'][i])

        
