import pandas as pd
import numpy as np
import math


#Cleaning data for PIC members list

members = pd.read_csv('DataScience/PaceInvestmentClub/Mailing_List/members_list.csv', encoding = 'latin1')

members = members.drop(['Middle Initial', 'Title', 'Phone','Mailing Address','Birthday'], axis =1)

members['Last Name'] = members['Last Name'].str.capitalize()

members['First Name'] = members['First Name'].str.capitalize()

members = members.rename(index=str, columns = {'Last Name':'Last','First Name':'First','Last Login':'Last_Login' ,'Join Date': 'Joined', 'Email Address': 'Email'})

members['Joined'] = pd.to_datetime(members['Joined'])

members['Last_Login'] = pd.to_datetime(members['Last_Login'])

new_members_list = members[(members['Joined'] > '2016-01-01')]

new_members_list.reset_index(inplace=True)

new_members_list =  new_members_list.drop('index', axis =1)

for index, row in new_members_list.iterrows():
    if row['Last'] == 'Caoimh':
        new_members_list.drop(index, inplace=True)

new_members_list

new_members_list[new_members_list['Joined'] == '2018-09-14']

<<<<<<< HEAD

=======
new_members_list.to_csv('DataScience/PaceInvestmentClub/Mailing_List/new_members_list.csv', index = False)
>>>>>>> 6d33bcc3a2e3304f2ac15e757b9a35c4f8843b85

new_members_list = pd.read_csv('new_members_list.csv')

new_members_list[(new_members_list['Joined'] > '2018-09-01')]

<<<<<<< HEAD
<<<<<<< HEAD
new_members_list[new_members_list['First'] == '']
=======
new_members_list.head()

df = pd.DataFrame({'Last':['Kane'],
                   'First':['Katie'],
                   'Groups':['New Accounts'],
                   'Joined':['2018-09-10'],
                   'Last_Login':['2018-09-10'],
                   'Email':['katiehkane@gmail.com']})

new_members_list = new_members_list.append(df, ignore_index = True, sort = False)

new_members_list.tail()

new_members_list.to_csv('new_members_list.csv', index = False)

new_members_list['First'].count()
>>>>>>> cb4ec790ed02f5e392402c93b8e366c20e959ec1
=======
new_members_list.head()

new_members_list = pd.read_csv('DataScience/PaceInvestmentClub/Mailing_List/new_members_list.csv')

df = pd.DataFrame({'Last':['Loomis'],
                   'First':['Savannah'],
                   'Groups':['New Accounts'],
                   'Joined':['2018-09-15'],
                   'Last_Login':['2018-09-15'],
                   'Email':['sl03680n@pace.edu']})

new_members_list = new_members_list.append(df, ignore_index = True, sort = False)

new_members_list[new_members_list['First'] == 'Savannah']

#new_members_list.drop(new_members_list.index[173], inplace=True)

new_members_list.head()
new_members_list.tail()

new_members_list.to_csv('DataScience/PaceInvestmentClub/Mailing_List/new_members_list.csv', index = False)
>>>>>>> 6d33bcc3a2e3304f2ac15e757b9a35c4f8843b85
