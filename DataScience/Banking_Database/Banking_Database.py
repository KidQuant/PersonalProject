import pandas as pd
import numpy as np

df = pd.read_csv('company_database.csv', encoding = 'latin1', index_col = False)

df.loc[0:60]

df[df['Company Name'] == 'Cowen Group']

networking = pd.read_csv('networking.csv')

networking.head()
networking.tail()
networking

del df5

df5 = pd.DataFrame({'Name':['Diana Yovera'],
                    'Firm':['Loop Capital Markets'],
                    'Location':['Chicago, Illinois'],
                    'Email':['diana.yovera@loopcapital.com'],
                    'Have Contacted?':['No'],
                    'Recieved Response?':['N/A'],
                    'Followed Up?':['N/A']})

networking  = networking.append(df5, ignore_index=True, sort=False)

networking.sort_values(by = ['Firm', 'Name'], inplace=True)

networking.duplicated().sum()

networking.drop_duplicates()

networking.to_csv('networking.csv', index = False)

networking

networking[networking['Firm'] == 'Cowen']

networking[-80]

networking['Location'][79:80] = 'Chicago, Illinois'
networking['Email'][57:58] = 'rebecca.mcadams@cowen.com'
networking['Have Contacted?'][55:56] = 'Yes'
networking['Recieved Response?'][55:56] = 'Yes - Automated Repsonse'
networking['Followed Up?'][55:56] = 'No'
networking[networking['Have Contacted?'] == 'Yes']
