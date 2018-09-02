import pandas as pd
import numpy as np

df = pd.read_csv('company_database.csv', encoding = 'latin1', index_col = False)

df.loc[0:60]

df[df['Company Name'] == 'Piper Jaffray']

networking = pd.read_csv('networking.csv')

networking.head()
networking.tail()

del df5

df5 = pd.DataFrame({'Name':['Katherine Jandric'],
                    'Firm':['Piper Jaffray'],
                    'Location':['Minneapolis, Minnesota'],
                    'Email':['katherine.jandric@pjc.com'],
                    'Have Contacted?':['No'],
                    'Recieved Response?':['N/A'],
                    'Followed Up?':['N/A']})

networking  = networking.append(df5, ignore_index=True, sort=False)

networking.sort_values(by = ['Firm', 'Name'], inplace=True)

networking.duplicated().sum()

networking.drop_duplicates()

networking.to_csv('networking.csv', index = False)

networking

networking[networking['Firm'] == 'Piper Jaffray']

networking[90:91]

networking['Location'][90:91] = 'Minneapolis, Minnesota'
networking['Have Contacted?'][98:99] = 'Yes'
networking['Recieved Response?'][98:99] = 'No'
networking['Followed Up?'][98:99] = 'Not Yet'
