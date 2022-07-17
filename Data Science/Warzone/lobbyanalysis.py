import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

engine=create_engine("mysql+mysqldb://root:root@localhost/Warzone")
my_conn = engine.connect()
query="SELECT * FROM qrissy"
df=pd.read_sql(query,my_conn)


lobbies = df[~df['Mode'].str.contains('rebirth')]
len(lobbies[lobbies['LobbyKD'] <= 1])/ len(lobbies)