import pandas as pd
import numpy as np

df = pd.read_csv('company_database.csv', encoding = 'latin1', index_col = False)

df.loc[29:29]

networking = pd.read_csv('networking.csv')

networking.head()
networking.tail()

del df5

df5 = pd.DataFrame({'Name':['Gabrielle DiBuono'],
                    'Firm':['Lazard'],
                    'Email':['gabrielle.dibuono@lazard.com'],
                    'Have Contacted?':['No'],
                    'Recieved Response?':['N/A'],
                    'Followed Up?':['N/A']})

networking  = networking.append(df5, ignore_index=True, sort=False)

networking.head()
networking.tail()

networking.sort_values(by = ['Firm'], inplace=True)

networking.duplicated()

networking.drop_duplicates()

networking.to_csv('networking.csv', index = False)
