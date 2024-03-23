import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

# db = mysql.connector.connect(
#     host = 'localhost',
#     user = 'Quants',
#     passwd = 'root',
#     database = 'test'
    
# )

# mycursor = db.cursor()
# mycursor.execute("SELECT * FROM huskers")




#########################################
#  Different Method
#########################################

user = 'bbreadman'

engine=create_engine("mysql+mysqldb://root:root@localhost/Warzone")
my_conn = engine.connect()
query="SELECT * FROM {} ORDER BY DATE DESC, TIME DESC".format(user)

df=pd.read_sql(query,my_conn)
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
df.sort_values(by=['Date'], ascending=False, inplace=False)
df[:15]

df.to_sql(con=my_conn, name=user, if_exists='replace', index=False)