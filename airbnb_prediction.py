import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')

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
