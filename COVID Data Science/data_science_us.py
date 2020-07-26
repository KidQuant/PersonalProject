import datetime
import time
import pandas as pd
import numpy as np
import wget


urls = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv']

[wget.download(url) for url in urls]

confirmed_df = pd.read_csv('time_series_covid19_confirmed_US.csv')
deaths_df = pd.read_csv('time_series_covid19_deaths_US.csv')

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
    value_name='Confirmed'
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

full_table['Active'] = full_table['Confirmed'] - full_table['Deaths']

full_grouped = full_table.groupby(['Date', 'Province_State'])[
    'Confirmed', 'Deaths', 'Active'].sum().reset_index()


temp = full_grouped.groupby(['Province_State', 'Date', ])['Confirmed', 'Deaths']
temp = temp.sum().diff().reset_index()

mask = temp['Province_State'] != temp['Province_State'].shift(1)

# renaming columns
temp.loc[mask, 'Confirmed'] = np.nan
temp.loc[mask, 'Deaths'] = np.nan

# renaming columns
temp.columns = ['Province_State', 'Date', 'New cases', 'New deaths']

# merging new values
full_grouped = pd.merge(full_grouped, temp, on=['Province_State', 'Date'])

# filling na with 0
full_grouped = full_grouped.fillna(0)

# fixing data types
cols = ['New cases', 'New deaths']
full_grouped[cols] = full_grouped[cols].astype('int')

#
full_grouped['New cases'] = full_grouped['New cases'].apply(
    lambda x: 0 if x < 0 else x)
full_grouped['New deaths'] = full_grouped['New deaths'].apply(
    lambda x: 0 if x < 0 else x)

full_grouped.drop(columns=['Active'], inplace=True)

full_grouped.sort_values(['Province_State', 'Date'], inplace=True)

today = time.strftime("%m-%d")

full_grouped.to_csv(
    r'covid-19-time-series-clean-complete-{}.csv'.format(today), index=False)
