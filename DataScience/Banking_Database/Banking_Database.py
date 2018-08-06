import pandas as pd
import numpy as np

df = pd.read_csv('company_database.csv', encoding = 'latin1', index_col = False)

df.loc[9:9]

networking = pd.read_csv('networking.csv')

networking.head()
networking.tail()

del df5

df5 = pd.DataFrame({'Name':['Marissa Frey', 'Cheyenne Dougherty', 'Camille Pasquier'],
                    'Firm':['Citigroup', 'Citigroup', 'Citigroup'],
                    'Location':['New York, New York', 'New York, New York', 'New York, New York'],
                    'Email':['jacqueline.waugh@citi.com', 'cheyenne.dougherty@citi.com', 'camille.pasquier@citi.com'],
                    'Have Contacted?':['No', 'No', 'No'],
                    'Recieved Response?':['N/A', 'N/A', 'N/A'],
                    'Followed Up?':['N/A', 'N/A', 'N/A']})

networking  = networking.append(df5, ignore_index=True, sort=False)

networking.tail()

networking.sort_values(by = ['Firm', 'Name'], inplace=True)

networking.duplicated().sum()

networking.drop_duplicates()

networking.to_csv('networking.csv', index = False)

networking
