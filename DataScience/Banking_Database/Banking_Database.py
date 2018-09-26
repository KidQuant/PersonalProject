import pandas as pd
import numpy as np

df = pd.read_csv('DataScience/Banking_Database/company_database.csv', encoding = 'latin1', index_col = False)

df.loc[0:60]

df[df['Company Name'] == 'Raymond James Financial Inc.']

networking = pd.read_csv('DataScience/Banking_Database/networking.csv')

networking.head()
networking.tail()

del df5

df = pd.DataFrame({'Name':['Grace Blankenship'],
                   'Firm':['Raymond James'],
                   'Location':['Tampa, Flordia'],
                   'Email':['grace.blankenship@raymondjames.com'],
                   'Have Contacted?':['No'],
                   'Recieved Response?':['N/A'],
                   'Followed Up?':['N/A']})

df.head()

networking  = networking.append(df, ignore_index= True, sort = False)

networking.head()

networking.sort_values(by = ['Firm', 'Name'], inplace=True)

networking.head()

networking.duplicated().sum()

#networking.drop(networking.index[81], inplace=True)

networking.to_csv('networking.csv', index = False)

networking

networking[networking['Firm'] == 'Raymond James']

networking['Location'][3:4] = 'Chicago, Illinois'
networking['Email'][57:58] = 'rebecca.mcadams@cowen.com'
networking['Have Contacted?'][81:82] = 'Yes'
networking['Recieved Response?'][81:82] = 'No'
networking['Followed Up?'][81:82] = 'No'
networking[(networking['Have Contacted?'] == 'Yes') & (networking['Firm'] == 'Lazard')]
