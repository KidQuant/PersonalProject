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

def get_best_squad(formation):
    FIFA18_copy = FIFA18.copy()
    store = []

    for i in formation:
        store.append([
        i,
        FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'] == i]['Overall'].idxmax()]]['Name'].to_string(index = False),
            FIFA18_copy[FIFA18_copy['Position'] == i]['Overall'].max(),
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'] == i]['Overall'].idxmax()]]['Age'].to_string(index = False),
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'] == i]['Overall'].idxmax()]]['Club'].to_string(index = False),
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'] == i]['Overall'].idxmax()]]['Value'].to_string(index = False),
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'] == i]['Overall'].idxmax()]]['Wage'].to_string(index = False)
        ])

        FIFA18_copy.drop(FIFA18_copy[FIFA18_copy['Position'] == i]['Overall'].idxmax(),
                         inplace = True)

    # return store with only necessary columns
    return pd.DataFrame(np.array(store).reshape(11,7),
                        columns = ['Position', 'Player', 'Overall', 'Age', 'Club', 'Value', 'Wage']).to_string(index = False)

squad_433 = ['GK', 'RB', 'CB', 'CB', 'LB', 'CDM', 'CM', 'CAM', 'RW', 'ST', 'LW']
print('4-3-3')
print(get_best_squad(squad_433))

squad_442 = ['GK', 'RB', 'CB', 'CB', 'LB', 'RM', 'CM', 'CM', 'LM', 'ST', 'ST']
print('4-4-2')
print(get_best_squad(squad_442))

squad_4231 = ['GK', 'RB', 'CB', 'CB', 'LB', 'CDM', 'CDM', 'CAM', 'CAM', 'CAM', 'ST']
print('4-2-3-1')
print(get_best_squad(squad_4231))

def get_best_squad_n(formation, nationality, measurement = 'Overall'):
    FIFA18_copy = FIFA18.copy()
    FIFA18_copy = FIFA18_copy[FIFA18_copy['Nationality'] == nationality]
    store = []

    for i in formation:
        store.append([
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'].str.contains(i)][measurement].idxmax()]]['Position'].to_string(index = False),
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'].str.contains(i)][measurement].idxmax()]]['Name'].to_string(index = False),
            FIFA18_copy[FIFA18_copy['Position'].str.contains(i)][measurement].max(),
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'].str.contains(i)][measurement].idxmax()]]['Age'].to_string(index = False),
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'].str.contains(i)][measurement].idxmax()]]['Club'].to_string(index = False),
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'].str.contains(i)][measurement].idxmax()]]['Value'].to_string(index = False),
            FIFA18_copy.loc[[FIFA18_copy[FIFA18_copy['Position'].str.contains(i)][measurement].idxmax()]]['Wage'].to_string(index = False)
        ])

        FIFA18_copy.drop(FIFA18_copy[FIFA18_copy['Position'].str.contains(i)][measurement].idxmax(),
                         inplace = True)

    return np.mean([x[2] for x in store]).round(2), pd.DataFrame(np.array(store).reshape(11,7),
                                                                 columns = ['Position', 'Player', measurement, 'Age', 'Club', 'Value', 'Wage']).to_string(index = False)

def get_summary_n(squad_list, squad_name, nationality_list):
    summary = []

    for i in nationality_list:
        count = 0
        for j in squad_list:

            # for overall rating
            O_temp_rating, _  = get_best_squad_n(formation = j, nationality = i, measurement = 'Overall')

            # for potential rating & corresponding value
            P_temp_rating, _ = get_best_squad_n(formation = j, nationality = i, measurement = 'Potential')

            summary.append([i, squad_name[count], O_temp_rating.round(2), P_temp_rating.round(2)])
            count += 1

    return summary

squad_343_strict = ['GK', 'CB', 'CB', 'CB', 'RB|RWB', 'CM|CDM', 'CM|CDM', 'LB|LWB', 'RM|RW', 'ST|CF', 'LM|LW']
squad_442_strict = ['GK', 'RB|RWB', 'CB', 'CB', 'LB|LWB', 'RM', 'CM|CDM', 'CM|CAM', 'LM', 'ST|CF', 'ST|CF']
squad_4312_strict = ['GK', 'RB|RWB', 'CB', 'CB', 'LB|LWB', 'CM|CDM', 'CM|CAM|CDM', 'CM|CAM|CDM', 'CAM|CF', 'ST|CF', 'ST|CF']
squad_433_strict = ['GK', 'RB|RWB', 'CB', 'CB', 'LB|LWB', 'CM|CDM', 'CM|CAM|CDM', 'CM|CAM|CDM', 'RM|RW', 'ST|CF', 'LM|LW']
squad_4231_strict = ['GK', 'RB|RWB', 'CB', 'CB', 'LB|LWB', 'CM|CDM', 'CM|CDM', 'RM|RW', 'CAM', 'LM|LW', 'ST|CF']

squad_list =[squad_343_strict, squad_442_strict, squad_4312_strict, squad_433_strict, squad_4231_strict]
squad_name = ['3-4-3', '4-4-2', '4-3-1-2', '4-3-3', '4-2-3-1']

France = pd.DataFrame(np.array(get_summary_n(squad_list, squad_name, ['France'])).reshape(-1,4), columns = ['Nationality', 'Squad', 'Overall', 'Potential'])
France.set_index('Nationality', inplace = True)
France[['Overall', 'Potential']] = France[['Overall', 'Potential']].astype(float)
print(France)
