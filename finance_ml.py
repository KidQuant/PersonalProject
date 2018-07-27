import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import bs4 as bs
import requests
import pickle
import os
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web


def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open('sp500tickers.pickle', 'wb') as f:
        pickle.dump(tickers, f)

    return tickers

save_sp500_tickers()

def get_data_from_morningstar(reload_sp500 = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open('sp500tickers.pickle', 'rb') as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000,1,1)
    end = dt.datetime.now()

    for ticker in tickers:
        print(ticker)

        if not os.path.exists('stock_dfs/{}csv'.format(ticker)):
            df = web.DataReader(ticker, 'morningstar', start, end)
            df.reset_index(inplace=True)
            df.set_index('Date', inplace=True)
            df = df.drop('Symbol', axis=1)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_morningstar()
