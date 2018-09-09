import numpy as np
import pandas as pd

subscribed = pd.read_csv('subscribed_members.csv')


subscribed = subscribed.drop(['OPTIN_TIME', 'CONFIRM_TIME', 'LATITUDE',
                              'LONGITUDE','GMTOFF','DSTOFF','CC','REGION',
                              'LAST_CHANGED','LEID','EUID','NOTES', 'OPTIN_IP','CONFIRM_IP'], axis = 1)

subscribed.head()
