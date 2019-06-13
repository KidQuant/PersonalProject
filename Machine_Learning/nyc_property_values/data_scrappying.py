import pandas as pd
import numpy as np
from tqdm import tqdm
import requests
import zipfile
import io

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 20)

rolling_sales_data = dict()

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

rpad_data_agglom = pd.concat([pd.read_csv('tcl.txt'), pd.read_csv('tc234.txt')], ignore_index = True) #Work on this part
