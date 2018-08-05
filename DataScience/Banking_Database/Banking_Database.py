import pandas as pd
import numpy as np

df = pd.read_csv('company_database.csv', encoding = 'latin1', index_col = False)

df.loc[1:3]

networking = pd.read_csv('networking.csv', index_col = 0)

networking.head()
networking.tail()

del df5

df5 = pd.DataFrame({'Name':['Courtney Goldsmith'],
                    'Firm':['Barclays'],
                    'Email':['courtney.goldsmith@barcap.com'],
                    'Have Contacted?':['No'],
                    'Recieved Response?':['N/A'],
                    'Followed Up?':['N/A']})

networking  = networking.append(df5, ignore_index=True, sort=False)

networking.head()
networking.tail()

networking.to_csv('networking.csv')
