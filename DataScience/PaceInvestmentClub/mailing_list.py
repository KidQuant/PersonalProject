import numpy as np
import pandas as pd

subscribed = pd.read_csv('subscribed_members.csv')

subscribed = subscribed.drop(['OPTIN_TIME','LATITUDE', 'LONGITUDE','GMTOFF','DSTOFF','CC','REGION',
                              'LAST_CHANGED','LEID','EUID','NOTES', 'OPTIN_IP','CONFIRM_IP', 'TIMEZONE'], axis = 1)

subscribed['First Name'] = subscribed['First Name'].str.capitalize()
subscribed['Last Name'] = subscribed['Last Name'].str.capitalize()

subscribed.head()


subscribed[(subscribed['First Name'] == 'Andre') & (subscribed['Last Name'] == 'Sealy')]

for index, row in subscribed.iterrows():
    if (row['First Name'] == 'Heeyun' and row['Last Name'] == 'Lee'):
        subscribed.drop(index, inplace=True)
    elif (row['First Name'] == 'Joey' and row['Last Name'] == 'Wong'):
        subscribed.drop(index, inplace=True)
    elif (row['First Name'] == 'Jeffrey' and row['Last Name'] == 'Leder'):
        subscribed.drop(index, inplace = True)
    elif (row['First Name'] == 'Ephraim' and row['Last Name'] == 'Agbenor'):
        subscribed.drop(index, inplace = True)
    elif (row['First Name'] == 'Andre' and row['Last Name'] == 'Sealy'):
        subscribed.drop(index, inplace=True)

subscribed[subscribed['MEMBER_RATING'] >= 3 ].count().MEMBER_RATING
