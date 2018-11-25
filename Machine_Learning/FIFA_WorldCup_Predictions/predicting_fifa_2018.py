import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.ticker as plticker
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

world_cup = pd.read_csv('Machine_Learning/FIFA_WorldCup_Predictions/World Cup 2018 Dataset.csv')
results = pd.read_csv('Machine_Learning/FIFA_WorldCup_Predictions/results.csv')

world_cup.head()

results.head()
results = results.drop(['neutral'], axis =1)

winner = []
for i in range (len(results['home_team'])):
    if results ['home_score'][i] > results['away_score'][i]:
        winner.append(results['home_team'][i])
    elif results['home_score'][i] < results['away_score'][i]:
        winner.append(results['away_team'][i])
    else:
        winner.append('Draw')
results['winning_team'] = winner

#adding goal difference column
results['goal_difference'] = np.absolute(results['home_score'] - results['away_score'])

results.head()

#working with a subset of the data one that includes games played by Nigeria in a Nigeria DataFrame
df = results[(results['home_team'] == 'Nigeria') | (results['away_team'] == 'Nigeria')]
nigeria = df.iloc[:]
nigeria.head()

year = []
for row in nigeria['date']:
    year.append(int(row[:4]))
nigeria['match_year'] = year
nigeria_1930 = nigeria[nigeria.match_year >= 1930]
nigeria_1930.count()

wins = []
for row in nigeria_1930['winning_team']:
    if row != 'Nigeria' and row != 'Draw':
        wins.append('Loss')
    else:
        wins.append(row)
winsdf = pd.DataFrame(wins, columns = ['Nigeria_Results'])

fig, ax = plt.subplots(1)
fig.set_size_inches(10.7,6.27)
sns.set(style = 'darkgrid')
sns.countplot(x = 'Nigeria_Results', data=winsdf)

worldcup_teams = ['Australia', 'Iran', 'Japan', 'Korea Republic',
                  'Saudi Arabia', 'Egypt', 'Morocco', 'Nigeria',
                  'Senegal', 'Tunisia', 'Costa Rica', 'Mexico',
                  'Panama', 'Argentina', 'Brazil', 'Colombia',
                  'Peru', 'Uruguay', 'Belgium', 'Croatia',
                  'Denmark', 'England', 'France', 'Germany',
                  'Iceland', 'Poland', 'Portugal', 'Russia',
                  'Serbia', 'Spain', 'Sweden', 'Switzerland']

df_teams_home = results[results['home_team'].isin(worldcup_teams)]
df_teams_away = results[results['away_team'].isin(worldcup_teams)]
df_teams = pd.concat((df_teams_home, df_teams_away))
df_teams.drop_duplicates()
df_teams.count()

df_teams.head()

year = []
for row in df_teams['date']:
    year.append(int(row[:4]))
df_teams['match_year'] = year
df_teams_1930 = df_teams[df_teams.match_year >= 1930]
df_teams_1930.head()

#dropping columns that will not affect match outcomes

df_teams_1930 = df_teams.drop(['date', 'home_score', 'away_score', 'tournament', 'city', 'country'
                              ,'goal_difference', 'match_year'], axis = 1)

df_teams_1930.head()

#Building the model
#The Predection label
#winning_team column shows '2' if home team wins, '1' if there was a tie, and '0' for a Loss

df_teams_1930 = df_teams_1930.reset_index(drop=True)
df_teams_1930.loc[df_teams_1930.winning_team == df_teams_1930.home_team, 'winning_team'] = 2
df_teams_1930.loc[df_teams_1930.winning_team == 'Draw', 'winning_team'] = 1
df_teams_1930.loc[df_teams_1930.winning_team == df_teams_1930.away_team, 'winning_team'] = 0

df_teams_1930.head()

#convert home team and away team from categorial variables to continous inputs
#get dummy variables

final = pd.get_dummies(df_teams_1930, prefix = ['home_team', 'away_team'], columns = ['home_team', 'away_team'])

#Separate X and Y sets
X = final.drop(['winning_team'], axis = 1)
y = final['winning_team']
y = y.astype('int')

#Seperate train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.30, random_state = 42)

final.head()
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
score = logreg.score(X_train, y_train)
score2 = logreg.score(X_test, y_test)

print('Training set accuracy ', '%.3f'%(score))
print('Test set accuracy ', '%.3f'%(score2))
