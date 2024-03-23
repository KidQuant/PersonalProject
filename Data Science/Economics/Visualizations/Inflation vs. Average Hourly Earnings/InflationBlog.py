import pandas as pd
import matplotlib.ticker as mtick
import matplotlib.gridspec as gridspec
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt


df = pd.read_csv('fredgraph.csv', )

df.head()
df.dtypes

df['DATE'] = pd.to_datetime(df['DATE'])
df.head()
df.tail()

ax = df.plot('DATE', 'AHETPI_PC1', label = 'Average Hourly Earnings', color = 'blue', xlim=('2001-02-01','2018-06-01'), figsize=(12,6))
df.plot('DATE','CPIAUCSL_PC1', label='CPI-U Inflation', color='red', xlim=('2001-02-01','2018-06-01'), ax=ax, figsize=(12,6) )
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.set_xlabel('Source: Bureau Labor of Statistics', style='italic', x=.89)
ax.set_title('Real Wages of Production and Nonsupervisory Employees', fontsize=18, x=.32)
ax.axvspan('2001-04-01', '2001-11-01', color='grey', alpha=0.5)
ax.axvspan('2008-01-01', '2009-07-01', color='grey', alpha=0.5)
plt.savefig('ahe.jpeg', bbox_inches='tight')

df2 = pd.read_csv('fredgraph2.csv')

df2['DATE'] = pd.to_datetime(df2['DATE'])

df2.head()
df2.tail()

ax1 = df2.plot('DATE', 'AHETPI_PC1', label='Average Hourly Earnings', color='blue', xlim=('2001-02-01','2018-06-01'), figsize=(12,6))
df2.plot('DATE', 'CPILFESL_PC1', label='Core CPI-U Inflation', color='red', xlim=('2001-02-01','2018-06-01'), figsize=(12,6), ax=ax1)
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.set_xlabel('Source: Bureau Labor of Statistics', style='italic', x=.89)
ax1.set_title('Real Wages of Production and Nonsupervisory Employees', fontsize=18, x=.32)
ax1.axvspan('2001-04-01', '2001-11-01', color='grey', alpha=0.5)
ax1.axvspan('2008-01-01', '2009-07-01', color='grey', alpha=0.5)
plt.savefig('ahecore.jpeg', bbox_inches='tight')


ax1 = df2.plot('DATE', 'AHETPI_PC1', label='Average Hourly Earnings', color='blue', xlim=('2001-02-01','2018-01-01'), figsize=(12,6))
df6.plot('DATE', 'GDPDEF_PC1', label='GDP Deflator', color='red', xlim=('2001-02-01','2018-01-01'), figsize=(12,6), ax=ax1)
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.set_xlabel('Source: Bureau of Economic Analysisi; Bureau of Labor Statistics', style='italic', x=.80)
ax1.set_title('Real Wages of Production and Nonsupervisory Employees', fontsize=18, x=.32)
ax1.axvspan('2001-04-01', '2001-11-01', color='grey', alpha=0.5)
ax1.axvspan('2008-01-01', '2009-07-01', color='grey', alpha=0.5)
plt.savefig('gdpdeflator.jpeg', bbox_inches='tight')


df3 = pd.read_csv('PCEPI.csv')
df3['DATE'] = pd.to_datetime(df['DATE'])

df3.head()
df3.tail()

df4 = pd.read_csv('PCEPILFE.csv')
df4['DATE'] = pd.to_datetime(df4['DATE'])

df4.head()


df5 = pd.read_csv('SUUR0000SA0.csv')

df5['DATE'] = pd.to_datetime(df5['DATE'])

df5.head()

df5.tail()


df6 = pd.read_csv('GDPDEF.csv')
df6['DATE'] = pd.to_datetime(df6['DATE'])
df6.head()
df6.tail()

df7 = pd.read_csv('MEDCPIM094SFRBCLE.csv')
df7['DATE'] = pd.to_datetime(df7['DATE'])

df7.head()
df7.tail()

df8 = pd.read_csv('TRMMEANCPIM094SFRBCLE.csv')
df8['DATE'] = pd.to_datetime(df8['DATE'])

df8.head()

df8.tail()

fig = plt.figure(figsize=(15,5))
fig.subplots_adjust(wspace=.02)

ax1 = plt.subplot2grid((1,2),(0,0))
ax1.plot(df['DATE'], df['AHETPI_PC1'], color='blue', label='Average Hourly Earnings')
df3.plot('DATE', 'PCEPI_PC1', color='red', label='PCE Chain-Type', ax=ax1, xlim=('2001-02-01','2018-06-01'))
ax1.set_xlabel(''); ax1.set_xticklabels(''); ax1.set_yticklabels(''); ax1.set_xticks([]); ax1.set_yticks([])

ax2 = plt.subplot2grid((1,2), (0,1))
ax2.plot(df['DATE'], df['AHETPI_PC1'], color = 'blue')
df4.plot('DATE', 'PCEPILFE_PC1', color = 'red', label = 'Core PCE Chain-Type', ax=ax2, xlim=('2001-02-01','2018-06-01'))
ax2.set_xlabel('Source: BEA', x=.87, style ='italic'); ax2.set_xticklabels(''); ax2.set_yticklabels(''); ax2.set_xticks([]); ax2.set_yticks([])
plt.title('Headline and Core PCE', fontsize=16,  x=-0.7)
plt.savefig('PCE.jpeg', bbox_inches='tight')

fig = plt.figure(figsize=(15,5))
fig.subplots_adjust(wspace=.02)

ax1 = plt.subplot2grid((1,2),(0,0))
ax1.plot(df['DATE'], df['AHETPI_PC1'], color='blue')
df7.plot('DATE', 'MEDCPIM094SFRBCLE_PC1', color='red', label='Median CPI', ax=ax1, xlim=('2001-02-01','2018-06-01'))
ax1.set_xlabel(''); ax1.set_xticklabels(''); ax1.set_yticklabels(''); ax1.set_xticks([]); ax1.set_yticks([])

ax2 = plt.subplot2grid((1,2), (0,1))
ax2.plot(df['DATE'], df['AHETPI_PC1'], color = 'blue')
df8.plot('DATE', 'TRMMEANCPIM094SFRBCLE_PC1', color = 'red', label = 'Trimmed-Mean', ax=ax2, xlim=('2001-02-01','2018-06-01'))
ax2.set_xlabel('Source: Federal Reserve', x=.8, style ='italic'); ax2.set_xticklabels(''); ax2.set_yticklabels(''); ax2.set_xticks([]); ax2.set_yticks([])
plt.title('Median CPI & Trimmed-Mean CPI', fontsize=16,  x=-0.7)
plt.savefig('trimmedmeanmedian.jpeg', bbox_inches='tight')



fig = plt.figure(figsize=(20,7))
fig.subplots_adjust(hspace=.05, wspace=.03)
gs1 = gridspec.GridSpec(4,4)
ax1 = plt.subplot2grid((2,4),(0,0))
ax1.plot(df['DATE'], df['AHETPI_PC1'], color = 'blue')
df.plot('DATE','CPIAUCSL_PC1',color='red', label='CPI-U', ax=ax1, xlim=('2001-02-01','2018-06-01'))
ax1.set_xlabel(''); ax1.set_xticklabels(''); ax1.set_yticklabels(''); ax1.set_xticks([]); ax1.set_yticks([])

ax2 = plt.subplot2grid((2,4), (1,0))
ax2.plot(df['DATE'], df['AHETPI_PC1'], color = 'blue')
df2.plot('DATE', 'CPILFESL_PC1', color='red', label='Core CPI-U', ax=ax2, xlim=('2001-02-01','2018-06-01'))
ax2.set_xlabel(''); ax2.set_xticklabels(''); ax2.set_yticklabels(''); ax2.set_xticks([]); ax2.set_yticks([])

ax3 = plt.subplot2grid((2,4), (0,1))
ax3.plot(df['DATE'], df['AHETPI_PC1'], color='blue')
df3.plot('DATE', 'PCEPI_PC1', color='red', label='PCE', ax=ax3, xlim=('2001-02-01','2018-05-01'))
ax3.set_xlabel(''); ax3.set_xticklabels(''); ax3.set_yticklabels(''); ax3.set_xticks([]); ax3.set_yticks([])

ax4 = plt.subplot2grid((2,4), (1,1))
ax4.plot(df['DATE'], df['AHETPI_PC1'], color='blue')
df4.plot('DATE', 'PCEPILFE_PC1', color='red', label='Core PCE', ax=ax4, xlim=('2001-02-01','2018-05-01'))
ax4.set_xlabel(''); ax4.set_xticklabels(''); ax4.set_yticklabels(''); ax4.set_xticks([]); ax4.set_yticks([])

ax5 = plt.subplot2grid((2,4), (0,2))
ax5.plot(df['DATE'], df['AHETPI_PC1'], color='blue')
df5.plot('DATE', 'SUUR0000SA0_PC1', color='red', label='Chained CPI', ax=ax5, xlim=('2001-02-01','2018-06-01'))
ax5.set_xlabel(''); ax5.set_xticklabels(''); ax5.set_yticklabels(''); ax5.set_xticks([]); ax5.set_yticks([])

ax6 = plt.subplot2grid((2,4), (1,2))
ax6.plot(df['DATE'], df['AHETPI_PC1'], color='blue')
df6.plot('DATE', 'GDPDEF_PC1', color = 'red', label = 'GDP Deflator', ax=ax6, xlim=('2001-02-01','2018-01-01'))
ax6.set_xlabel(''); ax6.set_xticklabels(''); ax6.set_yticklabels(''); ax6.set_xticks([]); ax6.set_yticks([]), ax6.set_xlim('2001-02-01','2018-01-01')

ax7 = plt.subplot2grid((2,4), (0,3))
ax7.plot(df['DATE'], df['AHETPI_PC1'], color = 'blue')
df7.plot('DATE', 'MEDCPIM094SFRBCLE_PC1', color='red', label='Median CPI', ax=ax7, xlim=('2001-02-01','2018-06-01'))
ax7.set_xlabel(''); ax7.set_xticklabels(''); ax7.set_yticklabels(''); ax7.set_xticks([]); ax7.set_yticks([])

ax8 = plt.subplot2grid((2,4),(1,3))
ax8.plot(df['DATE'], df['AHETPI_PC1'], color= 'blue')
df8.plot('DATE', 'TRMMEANCPIM094SFRBCLE_PC1', color = 'red', label = 'Trimmed-Mean CPI', ax=ax8, xlim=('2001-02-01','2018-06-01'))
ax8.set_xlabel(''); ax8.set_xticklabels(''); ax8.set_yticklabels(''); ax8.set_xticks([]); ax8.set_yticks([])
plt.title('The Many Different Inflation Metrics', fontsize=16, y=2.05, x=-2.6)
plt.xlabel('Source: BLS; BEA; Federal Reserve', style='italic')
plt.savefig('inflationindicies.jpeg', bbox_inches='tight')
