import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

df = pd.read_csv('train.csv.gz', sep=',').dropna()
df = df.sample(frac=0.01, random_state=99)

df.shape

count_classes = pd.value_counts(df['is_booking'], sort = True).sort_index()

count_classes.plot(kind = 'bar')
plt.title('Booking or Not booking')
plt.xlabel('Class')
plt.ylabel('Frequency')

df['date_time'] = pd.to_datetime(df['date_time'])
df['year'] = df['date_time'].dt.year
df['month'] = df['date_time'].dt.month

df['srch_ci'] = pd.to_datetime(df['srch_ci'], infer_datetime_format = True, errors = 'coerce')
df['srch_co'] = pd.to_datetime(df['srch_co'], infer_datetime_format = True, errors = 'coerce')

df['plan_time'] = ((df['srch_ci'] - df['date_time'])/np.timedelta64(1,'D')).astype(float)
df['hotel_nights'] = ((df['srch_co'] - df['srch_ci'])/np.timedelta64(1,'D')).astype(float)

cols_to_drop = ['date_time', 'srch_ci', 'srch_co', 'user_id']
df.drop(cols_to_drop, axis=1, inplace=True)

correlation = df.corr()
plt.figure(figsize=(18,18))
sns.heatmap(correlation, vmax=1, square=True, annot=True,cmap='viridis')
plt.title('Correlation between different features')

booking_indices = df[df.is_booking == 1].index
random_indices = np.random.choice(booking_indices, len(df.loc[df.is_booking == 1]), replace = False)
booking_sample = df.loc[random_indices]

not_booking = df[df.is_booking == 0].index
random_indices = np.random.choice(not_booking, sum(df['is_booking']), replace= False)
not_booking_sample = df.loc[random_indices]

df_new = pd.concat([not_booking_sample, booking_sample], axis = 0)

print('Percentage of not booking clicks: ', len(df_new[df_new.is_booking == 0]) / len(df_new))
print('Percentage of booking clicks: ', len(df_new[df_new.is_booking == 1]) / len(df_new))
print('Total number of records in resampled data: ', len(df_new))
