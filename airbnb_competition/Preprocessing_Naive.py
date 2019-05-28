
# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% Read the train and the test data
train_users = pd.read_csv('airbnb_competition/input/train_users_2.csv')
test_users = pd.read_csv('airbnb_competition/input/test_users.csv')

# Extracting labels from the train data
train_users_labels = train_users.loc[:,'country_destination']
print(train_users_labels.head(n=5))

# Extracting attributes from the train data
train_users_attrs = train_users.iloc[:, 0:15]
print(train_users_attrs.head(n=5))

train_users = train_users_attrs

train_users = train_users.drop(['date_first_booking'], axis =1)
test_users = test_users.drop(['date_first_booking'], axis=1)

# %% Date is split into 3 parts as year, month, and day in both test and train. These are added 
# new features in both test and train

date_acc_created = np.vstack(train_users.date_account_created.astype(str).apply(
    lambda x: list(map(int, x.split('-')))).values)
train_users['created_year'] = date_acc_created[:,0]
train_users['created_month'] = date_acc_created[:,1]
train_users['created_day'] = date_acc_created[:,2]
train_users = train_users.drop(['date_account_created'], axis=1)

date_acc_created_test = np.vstack(test_users.date_account_created.astype(str).apply(
    lambda x: list(map(int, x.split('-')))).values)
test_users['created_year'] = date_acc_created_test[:,0]
test_users['created_month'] = date_acc_created_test[:,1]
test_users['created_day'] = date_acc_created_test[:,2]
test_user = test_users.drop(['date_account_created'], axis=1)

