import pandas as pd
import matplotlib.ticker as mtick
import matplotlib.gridspec as gridspec
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt

start = dt.datetime(1996, 1,1)
end = dt.datetime.now()

df = pd.read_csv('Visualizations/Full_Employment/fredgraph.csv')



df['DATE'] = pd.to_datetime(df['DATE'])
df.head()



ax = df.plot('DATE','NILFWJN_UNEMPLOY', label = 'Unemployed + Not In Labor Force (Want a Job)', color = 'blue', xlim=('1994-01-01','2018-06-01'), figsize=(12,6))
ax.set_xlabel('Source: Bureau Labor of Statistics', style='italic', x=.89)
ax.set_title('Full Employment', fontsize=18, x=.05, y =1.01)
ax.axvspan('2001-04-01', '2001-11-01', color='grey', alpha=0.5)
ax.axvspan('2008-01-01', '2009-07-01', color='grey', alpha=0.5)
plt.savefig('Visualizations/Full_Employment/full_employment.jpeg', bbox_inches='tight')
