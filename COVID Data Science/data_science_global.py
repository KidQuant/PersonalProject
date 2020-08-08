import pandas as pd
import numpy as np
import datetime
import time
import wget
import os

###############################################
# Removing old files and extracting new ones
###############################################

globalFiles = ['time_series_covid19_confirmed_global.csv',
               'time_series_covid19_deaths_global.csv',
               'time_series_covid19_recovered_global.csv']

for data in globalFiles:
    if data in os.listdir():
        os.remove(data)

urls = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv']

[wget.download(url) for url in urls]

confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv')
recovered_df = pd.read_csv('time_series_covid19_recovered_global.csv')

###############################################
# Changing Data to include Hong Kong
###############################################

for x, y, z in zip(confirmed_df.index, deaths_df.index, recovered_df.index):
    if confirmed_df['Province/State'][x] == 'Hong Kong':
        confirmed_df.loc[x, ['Country/Region']] = 'Hong Kong'
    if deaths_df['Province/State'][y] == 'Hong Kong':
        deaths_df.loc[y, ['Country/Region']] = 'Hong Kong'
    if recovered_df['Province/State'][z] == 'Hong Kong':
        recovered_df.loc[z, ['Country/Region']] = 'Hong Kong'

###############################################
# Constructing and cleaning the data
###############################################

date = confirmed_df.columns[4:]

confirmed_df_long = confirmed_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=date,
    var_name='Date',
    value_name='Cases'
)

deaths_df_long = deaths_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=date,
    var_name='Date',
    value_name='Deaths'
)

recovered_df_long = recovered_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    value_vars=date,
    var_name='Date',
    value_name='Recovered'
)

recovered_df_long = recovered_df_long[recovered_df_long['Country/Region'] != 'Canada']

full_table = confirmed_df_long.merge(
    right=deaths_df_long,
    how='left',
    on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)

full_table = full_table.merge(
    right=recovered_df_long,
    how='left',
    on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)

full_table['Date'] = pd.to_datetime(full_table['Date'])

full_table['Recovered'] = full_table['Recovered'].fillna(0)

ship_rows = full_table['Province/State'].str.contains('Grand Princess') | full_table['Province/State'].str.contains(
    'Diamond Princess') | full_table['Country/Region'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('MS Zaandam')
full_ship = full_table[ship_rows]

full_table = full_table[~(ship_rows)]

full_table['Active'] = full_table['Cases'] - \
    full_table['Deaths'] - full_table['Recovered']

full_grouped = full_table.groupby(
    ['Date', 'Country/Region'])['Cases', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
temp = full_grouped.groupby(
    ['Country/Region', 'Date'])['Cases', 'Deaths', 'Recovered']
temp = temp.sum().diff().reset_index()

mask = temp['Country/Region'] != temp['Country/Region'].shift(1)

temp.loc[mask, 'Cases'] = np.nan
temp.loc[mask, 'Deaths'] = np.nan
temp.loc[mask, 'Recovered'] = np.nan

# renaming columns
temp.columns = ['Country/Region', 'Date',
                'New Cases', 'New Deaths', 'New Recovered']

# merging new values
full_grouped = pd.merge(full_grouped, temp, on=['Country/Region', 'Date'])

# filling na with 0
full_grouped = full_grouped.fillna(0)

# fixing data types
cols = ['New Cases', 'New Deaths', 'New Recovered']
full_grouped[cols] = full_grouped[cols].astype('int')
full_grouped['New Cases'] = full_grouped['New Cases'].apply(
    lambda x: 0 if x < 0 else x)

# cleaning the dataframe
full_grouped.drop(columns=['Active'], inplace=True)
full_grouped.sort_values(['Country/Region', 'Date'], inplace=True)

###############################################
# Saving based on the date
###############################################

# saving dataframe to csv
today = time.strftime('%m-%d')
full_grouped.to_csv(
    'covid-19-time-series-clean-global-{}.csv'.format(today), index=False)
