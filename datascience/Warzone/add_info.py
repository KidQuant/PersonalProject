import pandas as pd
import pickle
import os
from sqlalchemy import create_engine
from datetime import datetime


engine = create_engine("mysql+mysqldb://root:root@localhost/Warzone")
my_conn = engine.connect()

tag_query = "SELECT * FROM gamertags"
df = pd.read_sql(tag_query, my_conn)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by=['Date'], ascending=False, inplace=False)
df.to_sql(con=my_conn, name='teepe',
               if_exists='replace', index=False)




for i in gamerTags['User']:
    with open('User History/{}.pickle'.format(i), 'rb') as f:
        df = pickle.load(f)
        df['User'] = i

    with open('User History/{}.pickle'.format(i), 'wb') as f:
        pickle.dump(df, f)
        