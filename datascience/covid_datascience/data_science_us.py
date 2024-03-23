import datetime
import time
import pandas as pd
import numpy as np
import wget
import os


usFiles = ['time_series_covid19_confirmed_US.csv',
           'time_series_covid19_deaths_US.csv']
# %%
for data in usFiles:
    if data in os.listdir('Data'):
        os.remove(r'Data/{}'.format(data))

urls = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv']

[wget.download(url, out='Data') for url in urls]

confirmed_df = pd.read_csv('Data/time_series_covid19_confirmed_US.csv')
deaths_df = pd.read_csv('Data/time_series_covid19_deaths_US.csv')

confirmed_df.columns[:11]
deaths_df.columns[:12]

confirmed_df.drop(columns=['UID', 'iso2', 'iso3', 'code3',
                           'FIPS', 'Admin2', 'Combined_Key'], inplace=True)

deaths_df.drop(columns=['UID', 'iso2', 'iso3', 'code3',
                        'FIPS', 'Admin2', 'Combined_Key', 'Population'], inplace=True)

dates = confirmed_df.columns[4:]

confirmed_df_long = confirmed_df.melt(
    id_vars=['Province_State', 'Country_Region', 'Lat', 'Long_'],
    value_vars=dates,
    var_name='Date',
    value_name='Cases'
)
deaths_df_long = deaths_df.melt(
    id_vars=['Province_State', 'Country_Region', 'Lat', 'Long_'],
    value_vars=dates,
    var_name='Date',
    value_name='Deaths'
)

# Merging confirmed_df_long and deaths_df_long
full_table = confirmed_df_long.merge(
    right=deaths_df_long,
    how='left',
    on=['Province_State', 'Country_Region', 'Date', 'Lat', 'Long_']
)

full_table['Date'] = pd.to_datetime(full_table['Date'])

ship_rows = full_table['Province_State'].str.contains('Grand Princess') | full_table['Province_State'].str.contains(
    'Diamond Princess') | full_table['Country_Region'].str.contains('Diamond Princess') | full_table['Country_Region'].str.contains('MS Zaandam')
full_ship = full_table[ship_rows]

full_table = full_table[~(ship_rows)]

full_table['Active'] = full_table['Cases'] - full_table['Deaths']

full_grouped = full_table.groupby(['Date', 'Province_State'])[
    'Cases', 'Deaths', 'Active'].sum().reset_index()

temp = full_grouped.groupby(['Province_State', 'Date', ])['Cases', 'Deaths']
temp = temp.sum().diff().reset_index()

mask = temp['Province_State'] != temp['Province_State'].shift(1)

# renaming columns
temp.loc[mask, 'Cases'] = np.nan
temp.loc[mask, 'Deaths'] = np.nan

# renaming columns
temp.columns = ['Province_State', 'Date', 'New Cases', 'New Deaths']

# merging new values
full_grouped = pd.merge(full_grouped, temp, on=['Province_State', 'Date'])

# filling na with 0
full_grouped = full_grouped.fillna(0)

# fixing data types
cols = ['New Cases', 'New Deaths']
full_grouped[cols] = full_grouped[cols].astype('int')

#
full_grouped['New Cases'] = full_grouped['New Cases'].apply(
    lambda x: 0 if x < 0 else x)
full_grouped['New Deaths'] = full_grouped['New Deaths'].apply(
    lambda x: 0 if x < 0 else x)

full_grouped.drop(columns=['Active'], inplace=True)

full_grouped.sort_values(['Province_State', 'Date'], inplace=True)

today = time.strftime("%m-%d")

full_grouped.to_csv(
    r'Data/covid-19-time-series-clean-us-{}.csv'.format(today), index=False)
