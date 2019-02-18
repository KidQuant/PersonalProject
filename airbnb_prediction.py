import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
import datetime as dt


train_users = pd.read_csv('data/train_users_2.csv')
test_users = pd.read_csv('data/test_users.csv')

print('These were', train_users.shape[0], 'users in the training set and', test_users.shape[0], 'user in the test set.' )
print('In total there were', train_users.shape[0] +test_users.shape[0], 'users in total.')

df = pd.concat((train_users, test_users), axis = 0, ignore_index = True, sort = True)

display(df.isnull().sum())

df.gender.unique()

df.first_browser.unique()

df.gender.replace('-unknown-', np.nan, inplace=True)
df.first_browser.replace('-unknown-', np.nan, inplace=True)
df.drop('date_first_booking', axis= 1, inplace=True)

df.age.describe()

df.loc[df['age'] > 1000]['age'].describe()

df.loc[df['age'] < 18]['age'].describe()

df_with_year = df['age'] > 1000
df.loc[df_with_year, 'age'] = 2015 - df.loc[df_with_year, 'age']
df.loc[df_with_year, 'age'].describe()

df.loc[df.age > 95, 'age'] = np.nan
df.loc[df.age < 18, 'age'] = np.nan

plt.figure(figsize = (12,6))
sns.distplot(df.age.dropna(), rug=True)
sns.despine()
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x='country_destination', data=df)
plt.xlabel('Destination Country')
plt.ylabel('Number of users')
plt.show()

plt.figure(figsize=(12,6))
df_without_NDF = df[df['country_destination'] != 'NDF']
sns.boxplot(y='age', x='country_destination', data= df_without_NDF)
plt.xlabel('Destination Country')
plt.ylabel('Age of users')
plt.title('Country destination vs. Age')
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x='signup_method', data = df_without_NDF)
plt.xlabel('Signup Method')
plt.ylabel('Number of users')
plt.title('Users sign up method distribution')
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x='country_destination', data = df_without_NDF, hue='signup_method')
plt.xlabel('Destination Country')
plt.ylabel('Number of users')
plt.title('Users sign up method vs. destinations')
plt.legend(loc='upper right')
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x='signup_app',data=df_without_NDF)
plt.xlabel('Signup app')
plt.ylabel('Number of users')
plt.title('Signup app distribution')
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x='country_destination', data=df_without_NDF, hue='signup_app')
plt.xlabel('Destination Country')
plt.ylabel('Destination country based on signup app')
plt.legend(loc = ' upper right')
plt.show()

#Affliates

plt.figure(figsize= (18,6))
sns.countplot(x='first_device_type', data=df_without_NDF)
plt.xlabel('First device type')
plt.ylabel('Number of users')
plt.title('First device type distribution')
plt.show()

plt.figure(figsize=(18,6))
sns.countplot(x='country_destination', data=df_without_NDF, hue='first_device_type')
plt.ylabel('Number of users')
plt.xlabel('First device type vs. country destination')
plt.legend(loc = ' upper right')
plt.show()

df_without_NDF_US = df_without_NDF[df_without_NDF['country_destination'] != 'US']
plt.figure(figsize=(18,6))
sns.countplot(x='country_destination', data = df_without_NDF_US, hue = 'first_device_type')
plt.ylabel('Number of users')
plt.xlabel('First device type vs. country destination without the US')
plt.legend(loc='upper right')
plt.show()

plt.figure(figsize=(20,6))
sns.countplot(x = 'first_browser',data=df_without_NDF)
plt.xlabel('First Browser')
plt.ylabel('Number of users')
plt.title('First browser distribution')
plt.xticks(rotation=90)
plt.show()

#Users' Preferred Langauge

plt.figure(figsize=(12,6))
sns.countplot(x='language', data = df_without_NDF)
plt.xlabel('Langauge')
plt.ylabel('Number of users')
plt.title('Users language distribution')
plt.show()

#Dates

df_without_NDF.columns

df_without_NDF['date_account_created'] = pd.to_datetime(df_without_NDF['date_account_created'])
df_without_NDF['timestamp_first_active'] = pd.to_datetime((df_without_NDF.timestamp_first_active)//1000000, format='%Y%m%d')
df_without_NDF.date_account_created.value_counts().plot(kind = 'line', linewidth=1.2)

plt.figure(figsize=(12,6))
df_without_NDF.date_account_created.value_counts().plot(kind='line', linewidth=1.2)
plt.xlabel('Date')
plt.title('New account created over time')
plt.show()

df_2013 = df_without_NDF[df_without_NDF['timestamp_first_active'] > pd.to_datetime(20130101, format='%Y%m%d')]
df_2013 = df_2013[df_2013['timestamp_first_active'] < pd.to_datetime(20140101, format = '%Y%m%d')]

plt.figure(figsize=(12,6))
df_2013.timestamp_first_active.value_counts().plot(kind='line', linewidth='2')
plt.xlabel('Date')
plt.title('First active date 2013')
plt.show()

#Sessions

sessions = pd.read_csv('data/sessions.csv')

sessions.columns

len(sessions.user_id.unique())

print('There were', len(sessions.user_id.unique()), 'unique user id in the sessions data')

display(sessions.isnull().sum())

sessions.action_type.unique()

display(sessions.isnull().sum())

sessions.action_type.unique()

sessions.action_type.replace('-unknown-', np.nan, inplace = True)

sessions.action.value_counts().head(10)

sessions.action_type.value_counts().head(10)

sessions.action_detail.value_counts().head(10)

plt.figure(figsize=(18,6))
sns.countplot(x='device_type', data=sessions)
plt.xlabel('Device type')
plt.ylabel('Number of sessions')
plt.title('Device type distribution')
plt.xticks(rotation=90)
plt.show()

session_booked = pd.merge(df_without_NDF, sessions, how = 'left', left_on = 'id', right_on = 'user_id')
session_booked.columns

session_booked.action.value_counts().head(5)

#Predictive Modeling
train_users = pd.read_csv('data/train_users_2.csv')
test_users = pd.read_csv('data/test_users.csv')
df = pd.concat((train_users, test_users), axis = 0, ignore_index=True)
df.drop('date_first_booking', axis=1, inplace=True)

#Feature engineering

df['date_account_created'] = pd.to_datetime(df['date_account_created'])
df['timestamp_first_active'] = pd.to_datetime((df.timestamp_first_active // 1000000), format='%Y%m%d')

df['weekday_account_created'] = df.date_account_created.dt.weekday_name
df['day_account_created'] = df.date_account_created.dt.day
df['month_account_created'] = df.date_account_created.dt.month
df['year_account_created'] = df.date_account_created.dt.year

#Calculating the time lag variables

df['time_lag'] = (df['date_account_created'] - df['timestamp_first_active'])
df['time_lag'] = df['time_lag'].apply(lambda l: l.days)

df.drop(['date_account_created', 'timestamp_first_active'], axis = 1, inplace=True)

df['age'].fillna(-1, inplace=True)

sessions.rename(columns = {'user_id': 'id'}, inplace=True)

action_count = sessions.groupby(['id', 'action'])['secs_elapsed'].agg(len).unstack()
action_type_count = sessions.groupby(['id', 'action_type'])['secs_elapsed'].agg(len).unstack()
action_detail_count = sessions.groupby(['id', 'action_detail'])['secs_elapsed'].agg(len).unstack()
device_type_sum = sessions.groupby(['id', 'device_type'])['secs_elapsed'].agg(sum).unstack()

sessions_data = pd.concat([action_count, action_type_count, action_detail_count, device_type_sum],axis=1)
sessions_data.columns = sessions_data.columns.map(lambda x: str(x) + '_count')

#most used device
sessions_data['most_used_device'] = sessions.groupby('id')['device_type'].max()

print('There were', sessions.shape[0], 'recorded sessions in which there were', sessions.id.nunique(), 'unique users.')

sessions_data.index.names = ['id']
sessions_data.reset_index(inplace=True)

secs_elapsed = sessions.groupby('id')['secs_elapsed']

secs_elapsed = secs_elapsed.agg(
    {
        'secs_elapsed_sum': np.sum,
        'secs_elapsed_mean': np.mean,
        'secs_elapsed_min': np.min,
        'secs_elapsed_max': np.max,
        'secs_elapsed_median': np.median,
        'secs_elapsed_std': np.std,
        'secs_elapsed_var': np.var,
        'day_pauses': lambda x: (x > 86400).sum(),
        'long_pauses': lambda x: (x > 300000).sum(),
        'short_pauses': lambda x: (x < 3600).sum(),
        'session_length': np.count_nonzero
    }
)

secs_elapsed.reset_index(inplace=True)
sessions_secs_elapsed = pd.merge(sessions_data, secs_elapsed, on='id', how='left')
df = pd.merge(df, sessions_secs_elapsed, on = 'id', how = 'left')

print('There are', df.id.nunique(), 'users from the entire user data set that sessions information')

#Encoding the categorical feature
