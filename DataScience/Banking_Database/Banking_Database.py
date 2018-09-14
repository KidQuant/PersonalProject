import pandas as pd
import numpy as np

df = pd.read_csv('DataScience/Banking_Database/company_database.csv', encoding = 'latin1', index_col = False)

df.loc[0:60]

df[df['Company Name'] == 'SunTrust']

networking = pd.read_csv('DataScience/Banking_Database/networking.csv')

networking.head()
networking.tail()
networking

del df5

df5 = pd.DataFrame({'Name':['Michael Hasselt'],
                    'Firm':['Mizuho Bank'],
                    'Location':['New York, New York'],
                    'Email':['michael.hasselt@mizuhocbus.com'],
                    'Have Contacted?':['No'],
                    'Recieved Response?':['N/A'],
                    'Followed Up?':['N/A']})

networking  = networking.append(df5, ignore_index=True, sort=False)

networking.sort_values(by = ['Firm', 'Name'], inplace=True)

networking.duplicated().sum()

networking.drop(networking.index[81], inplace=True)

networking.to_csv('networking.csv', index = False)

networking

networking[networking['Firm'] == 'BB&T']

networking['Location'][3:4] = 'Chicago, Illinois'
networking['Email'][57:58] = 'rebecca.mcadams@cowen.com'
networking['Have Contacted?'][2:3] = 'No'
networking['Recieved Response?'][3:4] = 'No'
networking['Followed Up?'][3:4] = 'No'
networking[networking['Have Contacted?'] == 'Yes']
