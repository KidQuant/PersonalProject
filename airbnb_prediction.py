import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

train_users = pd.read_csv('train_users_2.csv')
test_user = pd.read_csv('test_users.csv')

print('These were', train_users.shape[0], 'users in the training set and', test_users.shape[0], 'user in the test set.' )
print('In total there were', train_users.shape[0] +test_users.shape[0], 'users in total.')

df = pd.concat((train_users, test_users), axis = 0, ignore_index = True, sort = True)
