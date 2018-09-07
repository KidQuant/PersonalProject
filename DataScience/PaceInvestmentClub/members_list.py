import pandas as pd
import numpy as np

members = pd.read_csv('members_list.csv', encoding = 'latin1', index_col = False)

members

members = members.drop(['Middle Initial', 'Title', 'Phone','Mailing Address','Birthday'], axis =1)

members

members['Last Name'] = members['Last Name'].str.capitalize()

members['First Name'] = members['First Name'].str.capitalize()

members

new_members_list = members.drop(members[members['Join Date'] < '2016-01-01'].index)

new_members_list.reset_index(inplace=True)

new_members_list

new_members_list.drop('index', axis =1, inplace=True)

new_members_list

new_members_list.to_csv('new_members_list.csv')
