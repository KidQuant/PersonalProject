import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sears_8cpn = pd.read_csv('Visualizations/sears_bankruptcy/sears_8cpn.csv')
sears_6cpn = pd.read_csv('Visualizations/sears_bankruptcy/sears_6cpn.csv')

sears_8cpn['Date'] = pd.to_datetime(sears_8cpn['Date'])
sears_6cpn['Date'] = pd.to_datetime(sears_6cpn['Date'])

sears_8cpn.dropna(inplace=True)
sears_6cpn.dropna(inplace=True)

sears_8cpn.head()
sears_6cpn.head()

sears_8cpn.tail()
sears_6cpn.tail()

labels = ['Jun 17', 'Jul 17', 'Aug 17', 'Sep 17', 'Oct 17', 'Nov 17', 'Dec 17', 'Jun 18', 'Jul 18', 'Aug 18', 'Sep 18', 'Oct 18']

ax = sears_6cpn.plot('Date', '6.625% Coupon', label = '6.625% Coupon (12/19 Maturity)', color = 'Blue', xlim = ('2017-09-25', '2018-10-15'), figsize = (11,6))
sears_8cpn.plot('Date', '8% Coupon', label = '8.0% Coupon (10/18 Maturity)', color = 'Red', xlim = ('2017-10-15', '2018-10-15'), ax=ax)
ax.set_title('Prices on Outstanding Public Debt: Sears', fontsize = 18, x=.25, y=1.02)
ax.set_xlabel('Source: Bloomberg', style = 'italic', x=0.95)
ax.legend(fontsize = 10)
plt.savefig('Visualizations/sears_bankruptcy/Outstanding_Debt.jpeg', bbox_inches = 'tight')
