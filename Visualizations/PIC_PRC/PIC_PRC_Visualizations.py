import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.gridspec as gridspec

deficit = pd.read_csv('Visualizations\PIC_PRC\FYFSD.csv')
df = deficit[80:]
df

ax = df.plot('DATE', 'FYFSD', kind ='bar', color = 'blue', figsize = (12,6), label = 'Defict/Surplus' )
ax.set_xlabel('Source: U.S. Treasury Department', style='italic', x=.89)
ax.set_title('Surplus/Deficit After Tax Bill', fontsize=25, x=.2)



df2 = pd.read_csv('Visualizations\PIC_PRC\GFDEGDQ188S.csv')

df2['DATE'] = pd.to_datetime(df2['DATE'])

ax1 = df2.plot('DATE', 'GFDEGDQ188S', label = 'Debt To GDP', color ='blue', xlim = ('1966-01-01', '18-06-01'), figsize = (12,6))
ax1.set_title('Public Debt As A Percentage of GDP', fontsize=18, x=.2)
ax1.axvspan('1970-01-01', '1971-01-01', color='grey', alpha=0.5)
ax1.axvspan('1973-09-01', '1975-06-01', color='grey', alpha=0.5)
ax1.axvspan('1980-01-01', '1980-09-01', color='grey', alpha=0.5)
ax1.axvspan('1981-09-01', '1982-12-01', color='grey', alpha=0.5)
ax1.axvspan('1990-09-01', '1991-03-01', color='grey', alpha=0.5)
ax1.axvspan('01-04-01', '01-11-01', color='grey', alpha=0.5)
ax1.axvspan('08-01-01', '09-07-01', color='grey', alpha=0.5)
ax1.set_xlabel('Source: Federal Reserve Bank of St. Louis', style='italic', x=.75)

#Disposable Income

df3 = pd.read_csv('Visualizations\PIC_PRC\DSPIC96.csv')

df3['DATE'] = pd.to_datetime(df3['DATE'])

df3.head()
df3.tail()

ax2 = df3.plot('DATE', 'DSPIC96_PC1', label = 'Disposable Income', color = 'blue', xlim = ('00-01-01','18-09-01'), figsize = (12,6))
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
ax2.set_xlabel('Source: Bureau of Economic Analysis', style='italic', x=.75)
ax2.axvspan('01-04-01', '01-11-01', color='grey', alpha=0.5)
ax2.axvspan('08-01-01', '09-07-01', color='grey', alpha=0.5)
ax2.legend('')

#GDP Growth

df4 = pd.read_csv('Visualizations\PIC_PRC\GDPC1.csv')
df4['DATE'] = pd.to_datetime(df4['DATE'])

df4 = df4[6:].reset_index()
df4.drop(['index'], axis = 1, inplace = True)
after = df4.copy()

df4.head()
after.head()

df4.tail()
after.tail()

after['GDPC1_PCA'][0:14] = 0
df4['GDPC1_PCA'][14:] = 0



labels = ['Q2 14', 'Q3 14', 'Q4 14',
          'Q1 15', 'Q2 15', 'Q3 15', 'Q4 15',
          'Q1 16', 'Q2 16', 'Q3 16', 'Q4 16',
          'Q1 17', 'Q2 17', 'Q3 17', 'Q4 17',
          'Q1 18', 'Q2 18', 'Q3 18']

ax3 = df4.plot('DATE', 'GDPC1_PCA', label = 'Real GDP Growth', color = 'blue', xlim = ('13-01-10','18-01-01'), figsize = (13,6), kind = 'bar', width =.8)
after.plot('DATE', 'GDPC1_PCA',  ax=ax3,  color = 'green', kind = 'bar', width =.8)
ax3.yaxis.set_major_formatter(mtick.PercentFormatter())
ax3.set_xticklabels(labels,rotation=0)
ax3.legend('')
ax3.set_xlabel('Source: Bureau of Economic Analysis', style='italic', x=.80)
