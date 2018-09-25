import pandas as pd
import numpy as np

df = pd.read_csv('DataScience/Banking_Database/company_database.csv', encoding = 'latin1', index_col = False)

df.loc[0:60]

df[df['Company Name'] == 'Duff & Phelps']

networking = pd.read_csv('DataScience/Banking_Database/networking.csv')

networking.head()
networking.tail()

del df5

df = pd.DataFrame({'Name':['Melinda Pesapane'],
                   'Firm':['Duff & Phelps'],
                   'Location':['New York, New York'],
                   'Email':['melinda.pesapane@duffandphelps.com'],
                   'Have Contacted?':['No'],
                   'Recieved Response?':['N/A'],
                   'Followed Up?':['N/A']})

df = df[['Name','Firm','Location','Email','Have Contacted?','Recieved Response?','Followed Up?']]

df.head()

networking  = networking.append(df, ignore_index= True)

networking.sort_values(by = ['Name', 'Firm'], inplace=True)

networking = networking[['Name', 'Firm', 'Location', 'Email', 'Have Contacted?', 'Recieved Response?', 'Followed Up?']]

networking.duplicated().sum()

#networking.drop(networking.index[81], inplace=True)

networking.to_csv('networking.csv', index = False)

networking

networking[networking['Firm'] == 'Duff & Phelps']

networking['Location'][3:4] = 'Chicago, Illinois'
networking['Email'][57:58] = 'rebecca.mcadams@cowen.com'
networking['Have Contacted?'][77:78] = 'Yes'
networking['Recieved Response?'][77:78] = 'No'
networking['Followed Up?'][77:78] = 'No'
networking[(networking['Have Contacted?'] == 'Yes') & (networking['Firm'] == 'Lazard')]
