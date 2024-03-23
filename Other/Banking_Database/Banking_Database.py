import pandas as pd
import numpy as np

df = pd.read_csv('DataScience/Banking_Database/company_database.csv', encoding = 'latin1', index_col = False)

df.head()

df.loc[10:15]

df[df['Company Name'] == 'SunTrust']

networking = pd.read_csv('DataScience/Banking_Database/networking.csv')

networking.head()
networking.tail()

del df5

df2 = pd.DataFrame({'Name':['Jocelyn Jackson'],
                   'Firm':['SunTrust Bank'],
                   'Location':['Atlanta, Georgia'],
                   'Email':['jocelyn.jackson@suntrust.com'],
                   'Have Contacted?':['No'],
                   'Recieved Response?':['N/A'],
                   'Followed Up?':['N/A']})

df2.head()


networking  = networking.append(df2, ignore_index= True, sort = False)

networking.sort_values(by = ['Firm', 'Name'], inplace=True)

networking.head()

networking.duplicated().sum()

#networking.drop(networking.index[81], inplace=True)

networking.to_csv('networking.csv', index = False)

networking[networking['Firm'] == 'SunTrust Bank']

networking['Location'][3:4] = 'Chicago, Illinois'
networking['Email'][57:58] = 'rebecca.mcadams@cowen.com'
networking['Have Contacted?'][77:78] = 'Yes'
networking['Recieved Response?'][76:77] = 'No'
networking['Followed Up?'][81:82] = 'No'
networking[(networking['Have Contacted?'] == 'Yes') & (networking['Firm'] == 'Lazard')]
