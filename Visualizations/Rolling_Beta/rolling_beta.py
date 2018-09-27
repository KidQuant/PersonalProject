import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hardware = pd.read_csv('Visualizations/Rolling_Beta/hardware.csv')
internet = pd.read_csv('Visualizations/Rolling_Beta/internet.csv')
software = pd.read_csv('Visualizations/Rolling_Beta/software.csv')
semiconductor = pd.read_csv('Visualizations/Rolling_Beta/semiconductor.csv')

hardware['Date'] = pd.to_datetime(hardware['Date'])
internet['Date'] = pd.to_datetime(internet['Date'])
software['Date'] = pd.to_datetime(software['Date'])
semiconductor['Date'] = pd.to_datetime(semiconductor['Date'])

hardware.tail()

ax = hardware.plot('Date', 'Hardware', label = 'Hardware', color ='Blue', xlim=('2010-01-20','2018-09-13'), figsize = (11,6))
internet.plot('Date','Internet', label = 'Internet', color = 'red', xlim=('2010-01-20','2018-09-13'), ax=ax )
software.plot('Date','Software', label = 'Software', color = 'orange', xlim =('2010-01-20','2018-09-13'), ax=ax)
semiconductor.plot('Date', 'Semiconductor', label = 'Semiconductor', color='green', xlim =('2010-01-20','2018-09-13'), ax=ax)
ax.set_title('Rolling Beta for Technology Sector', fontsize= 18, x = .2, y=1.02 )
ax.set_xlabel('Source: Bloomberg LP', style = 'italic', x=.9, y=.9)
ax.legend(fontsize=10)
plt.savefig('Visualizations/Rolling_Beta/rolling_beta.jpeg', bbox_inches='tight')
