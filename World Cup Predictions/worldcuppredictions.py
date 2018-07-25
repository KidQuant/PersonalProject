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

FIFA18['Position'] = FIFA18['Preferred Positions'].str.split().str[0]

plt.figure(figsize=(16,8))
sns.set_style('whitegrid')
plt.title('Grouping player by Age', fontsize=30, fontweight='bold', y=1.05)
plt.xlabel('Number of players', fontsize=25)
plt.ylabel('Players Age', fontsize=25)
sns.countplot(x='Age', data=FIFA18, palette='hls')
plt.show()

plt.figure(figsize=(16,8))
sns.set_style('whitegrid')
plt.title('Grouping players by Overall', fontsize=30, fontweight='bold', y=1.05)
plt.xlabel('Number of players', fontsize=25)
plt.ylabel('Players Age', fontsize=25)
sns.countplot(x='Overall', data=FIFA18, palette='hls')
plt.show()

plt.figure(figsize=(16,8))
sns.set_style('whitegrid')
plt.title('Grouping players by Preferred Position', fontsize=30, fontweight='bold', y=1.05)
plt.xlabel('Number of players', fontsize=25)
plt.ylabel('Players Age', fontsize=25)
sns.countplot(x='Position', data=FIFA18, palette='hls')
plt.show()

FIFA18['Nationality'].value_counts().head(25)

sorted_players = FIFA18.sort_values(['ValueNum'], ascending= False).head(20)
players = sorted_players[['Name', 'Age', 'Nationality', 'Club', 'Position', 'Value']].values

from IPython.display import HTML, display

table_content = ''
for row in players:
    HTML_row = '<tr>'
    HTML_row += '<td>' + str(row[0]) + '</td>'
    HTML_row += '<td>' + str(row[1]) + '</td>'
    HTML_row += '<td>' + str(row[2]) + '</td>'
    HTML_row += '<td>' + str(row[3]) + '</td>'
    HTML_row += '<td>' + str(row[4]) + '</td>'
    HTML_row += '<td>' + str(row[5]) + '</td>'

    table_content += HTML_row + '</tr>'

display(HTML(
    '<table><tr><th>Name</th><th>Age</th><th>Nationality</th><th>Club</th><th>Position</th><th>Value</th></tr>{}</table>'.format(table_content))
)

plt.figure(figsize=(16,8))
sns.set_style('whitegrid')
plt.title('Players Value according to their Age and Overall', fontsize=30, fontweight='bold', y=1.05)
plt.xlabel('Age', fontsize=25)
plt.ylabel('Overall', fontsize=25)

age = FIFA18['Age'].values
overall = FIFA18['Overall'].values
value = FIFA18['ValueNum'].values

plt.scatter(age, overall, s = value/10000, edgecolors='black')
plt.show()

sorted_players = FIFA18.sort_values(['WageNum'], ascending=False).head(20)
players = sorted_players[['Name', 'Age', 'Nationality', 'Club', 'Position', 'Wage']].values

from IPython.display import HTML, display

table_content = ''
for row in players:
    HTML_row = '<tr>'
    HTML_row += '<td>' + str(row[0]) + '</td>'
    HTML_row += '<td>' + str(row[1]) + '</td>'
    HTML_row += '<td>' + str(row[2]) + '</td>'
    HTML_row += '<td>' + str(row[3]) + '</td>'
    HTML_row += '<td>' + str(row[4]) + '</td>'
    HTML_row += '<td>' + str(row[5]) + '</td>'

    table_content += HTML_row + '</tr>'

display(HTML(
    '<table><tr><th>Name</th><th>Age</th><th>Nationality</th><th>Club</th><th>Position</th><th>Wage</th></tr>{}</table>'.format(table_content))
)

plt.figure(figsize=(16,8))
sns.set_style('whitegrid')
plt.title('Player Wage according to their Age and Overall', fontsize=30, fontweight='bold', y=1.05)
plt.xlabel('Age', fontsize=25)
plt.ylabel('Overall', fontsize= 25)
age = FIFA18['Age'].values
overall = FIFA18['Overall'].values
value = FIFA18['WageNum'].values

plt.scatter(age, overall, s = value/500, edgecolors='black', color='red')
plt.show()

FIFA18 = FIFA18[['Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Position', 'Value', 'Wage']]
FIFA18.head(10)
