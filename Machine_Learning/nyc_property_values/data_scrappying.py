
#%% Importing packages and setting the row/column size for dataframes

import pandas as pd
import numpy as np
from tqdm import tqdm
import requests
import zipfile
import io

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 20)

rolling_sales_data = dict()

#%% Extracting the rolling sales data

rolling_sales_data_key_pairs = {'Manhattan': 'manhattan',
                                'Brooklyn': 'brooklyn',
                                'Queens': 'queens',
                                'Bronx': 'bronx',
                                'Staten Island': 'statenisland'}

for b_k, b_xls in tqdm(list(rolling_sales_data_key_pairs.items())):
    borough_rsd = pd.read_excel('https://www1.nyc.gov/assets/finance/downloads/pdf/rolling_sales/rollingsales_{0}.xls'.format(b_xls))
    borough_rsd.columns = borough_rsd.iloc[3].values
    borough_rsd = borough_rsd[4:]
    rolling_sales_data[b_k] = borough_rsd

r = requests.get('http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyc_pluto_16v1.zip')
pluto_key_pairs = {'Manhattan': 'MN.csv',
                   'Brooklyn': 'BK.csv',
                   'Bronx': 'BX.csv',
                   'Staten Island': 'SI.csv',
                   'Queens': 'QN.csv'}
pluto_data = dict()
for b_k, b_csv in tqdm(list(pluto_key_pairs.items())):
    with zipfile.ZipFile(io.BytesIO(r.content)) as ar:
        borough_pluto = pd.read_csv(ar.open(b_csv))
        pluto_data[b_k] = borough_pluto

rolling_sales_agglom = pd.DataFrame(columns = rolling_sales_data['Manhattan'].columns)
pluto_data_agglom = pd.DataFrame(columns = pluto_data['Manhattan'].columns)
for b_k in tqdm(pluto_key_pairs.keys()):
    pluto_data[b_k]['Borough'] = rolling_sales_data[b_k]['Borough'] = b_k
    rolling_sales_agglom = pd.concat([rolling_sales_agglom, rolling_sales_data[b_k]], ignore_index = True)
    pluto_data_agglom = pd.concat([pluto_data_agglom, pluto_data[b_k]], ignore_index = True)
del rolling_sales_agglom['BOROUGH']

%ls

rpad_data_agglom = pd.concat([pd.read_csv('tcl.txt',  error_bad_lines=False), 
        pd.read_csv('tc234.txt', error_bad_lines=False)], ignore_index = True) #Work on this part


#%% Merging

rolling_sales_agglom.columns = [c.title().replace(' ', '') for x in list(rolling_sales_agglom.columns)]

# rolling_sales_agglom = rolling_sales_agglom[rolling_sales_agglom['SalePrice'] > 1000]

rs_a_f = rolling_sales_agglom[rolling_sales_agglom['ApartmentNumber'] == '            ']

rs_a_f = rs_a_f[rs_a_f['LandSquareFeet'] > 0]

# This function is a doozy! Here' what it does, step-by-step:
# 1. Select our desired slice of the variables from the rolling sales data.
# 2. Aggregate by Borough-Block-Lot, creating a groupby object.
# 3. Merge the non-key variables via summation, converting the groupby object to the hierarchical DataFrame.
# 4. Reset the index to shake off the hierarchical index and recreate a simple numerical one.
# 5. Assign all of that to rs_a_ff.
rs_a_ff = rs_a_f[['Borough', 'Block', 'Lot', 'SalePrice', 'LandSquareFeet']].groupby(by=['Borough', 'Block', 'Lot']).sum().reset_index()
# Now all that's left is to create a new column for market value by broadcasting division.
rs_a_ff['MarketValueSqFt'] = rs_a_ff['SalePrice'] / rs_a_ff['LandSquareFeet']

len(rs_a_f) - len(rs_a_ff)

rolling_pluto = pd.merge(rs_a_ff, pluto_data_agglom,
                         how='outer', on=['Borough', 'Block', 'Lot'])

len(rolling_pluto) - len(pluto_data_agglom)

len(rs_a_ff) - len(rolling_pluto[rolling_pluto['SalePrice'] >= 0])

rpad_key_pairs = {1.0: 'Manhattan',
                  2.0: 'Bronx',
                  3.0: 'Brooklyn',
                  4.0: 'Queens',
                  5.0: 'Staten Island',
                 }
rpad_data_agglom['Borough'] = rpad_data_agglom['BORO'].apply(lambda n: rpad_key_pairs[n])
del rpad_data_agglom['BORO']

rpad_data_agglom.columns = [c.title().replace('_', '') for c in list(rpad_data_agglom.columns)]

rpad_data_agglom.head(5)

rpad_columns_of_interest = ['Borough', 'Block', 'Lot', 'CurFvT', 'NewFvT', 'CuravtA']

counts = rpad_data_agglom.groupby(by=['Borough', 'Block', 'Lot']).count().reset_index()

counts = counts.sort_values(by='CurFvT', ascending=False)
counts[counts['Bble'] > 1]

rpad_data_agglom.groupby(by=['Borough', 'Block', 'Lot']).count()

rpad_data_agglom[(rpad_data_agglom['Borough'] == 'Bronx') &
                 (rpad_data_agglom['Block'] == 2260) &
                 (rpad_data_agglom['Lot'] == 62)]

rpad_data_agglom_f = rpad_data_agglom[rpad_data_agglom['Ease'].isnull()]

rolling_pluto_rpad = pd.merge(rolling_pluto, rpad_data_agglom_f[rpad_columns_of_interest],
                              how='inner', on=['Borough', 'Block', 'Lot'])


len(rolling_pluto_rpad) - len(rolling_pluto)

(len(rolling_pluto_rpad) - len(rolling_pluto)) / len(rolling_pluto_rpad)

#%% Cleaning 

rolling_pluto_rpad['BldgArea'].value_counts()[0.0]

rolling_pluto_rpad = rolling_pluto_rpad[rolling_pluto_rpad['BldgArea'] > 0]

rolling_pluto_rpad = rolling_pluto_rpad[rolling_pluto_rpad['Address'].notnull()]

# len(rolling_pluto_rpad[rolling_pluto_rpad['CT2010'] == '       '])

# len(rolling_pluto_rpad[rolling_pluto_rpad['CB2010'] == '     '])

def convert_floats_and_whitespace_strings_to_floats_and_strings(series):
    l = []
    for entry in [str(entry).strip() for entry in series]:
        if entry == "":
            l.append(np.nan)
        else:
            try:
                l.append(float(entry))
            except ValueError:
                l.append(entry)
    return l

columns_needing_fixing = rolling_pluto_rpad.columns
for column in columns_needing_fixing:
    rolling_pluto_rpad[column] = convert_floats_and_whitespace_strings_to_floats_and_strings(rolling_pluto_rpad[column])

# rolling_pluto_rpad['CT2010'].dtype

# rolling_pluto_rpad['CB2010'].dtype

#%% Partition

r_p_pre = rolling_pluto_rpad[rolling_pluto_rpad['SalePrice'].notnull()]
r_p_post = rolling_pluto_rpad[rolling_pluto_rpad['SalePrice'].isnull()]

# Ignore the warning.
mkt_sqft_values = r_p_pre['SalePrice'] / r_p_pre['BldgArea']
r_p_pre['MarketValueSqFt'] = mkt_sqft_values
r_p_post['MarketValueSqFt'] = np.nan


# Ignore the warning.
for partition in [r_p_pre, r_p_post]:    
    assessed_sqft_values = partition['CuravtA'] / partition['BldgArea']
    pre_assessed_mkt_values = partition['CurFvT'] / partition['BldgArea']
    post_assessed_mkt_values = partition['NewFvT'] / partition['BldgArea']
    partition['AssessmentValueSqFt'] = assessed_sqft_values
    partition['EstPriorMarketValueSqFt'] = pre_assessed_mkt_values
    partition['EstCurentMarketValueSqFt'] = post_assessed_mkt_values

r_p_pre.reset_index(drop=True, inplace=True)
r_p_post.reset_index(drop=True, inplace=True)

r_p_pre.index.name = r_p_post.index.name = 'Index'

r_p_pre.to_csv('nyc_building_sales.csv')
r_p_post.to_csv('nyc_building_nonsales.csv')