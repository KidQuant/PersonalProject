import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gaming_trends = pd.DataFrame({'Average MAU': [65, 140, 190, 225, 260, 295,335,360],
                              'Mobile Average MAU': [25, 70, 135, 185, 225, 248, 265, 330]},
                              index = ['2015A','2016A','2017A','2018E','2019E','2020E','2021E','2022E'])

gaming_trends.plot(kind='bar', figsize = (11,5), ylim = (0, 500), width = .8)
plt.title('China Live Game Streaming MAU Forecast', x=.3, y=1.02, fontsize=20)
plt.ylabel('In Millions', fontsize = 12)
plt.xticks(rotation =0)
plt.xlabel('Source: Huya F-1; Bloomberg', x=0.9,style='italic')
plt.savefig('Visualizations/Gaming_Visuals/gaming_trends.jpeg', bbox_inches='tight')


headset_trends = pd.DataFrame({'Gaming Peripheral': [1.5, 2.3, 2.9, 3.3, 4.2, 4.6, 5.9]},
                              index = ['2014A','2015A','2016A','2017A','2018E','2020E','2021E'])

headset_trends.plot(kind = 'bar', figsize=(11,5), width= .8)
plt.title('Online Gaming Peripheral Market', x = .25, y=1.02, fontsize=20)
plt.xlabel('Source: Newzoo; Bloomberg', x=0.9, style='italic')
plt.xticks(rotation=0, fontsize=11)
plt.ylabel('In Billions', fontsize=12)
plt.savefig('Visualizations/Gaming_Visuals/gaming_peripherals.jpeg', bbox_inches='tight')

turtle_beach = pd.read_csv('Visualizations/Gaming_Visuals/Hear_Inventory.csv')

turtle_beach

total_inventory = turtle_beach.drop('Inv_Days_Out.', axis =1)

total_inventory

total_inventory = total_inventory.rename(index = str, columns = {'Inv.':'Total Inventory'})
Inv_Days_Out = turtle_beach.drop('Inv.', axis=1)


inv_days_out = Inv_Days_Out.rename(index = str, columns = {'Inv_Days_Out.':'Inventory Days Outstanding'})

total_inventory

labels = ['Q4 2015', 'Q1 2016', 'Q2 2016', 'Q3 2016', 'Q4 2016',
          'Q1 2017', 'Q2 2017', 'Q3 2017', 'Q4 2017', 'Q1 2018',
          'Q2 2018']

ax = total_inventory.plot('Date', 'Total Inventory',color= 'blue',  kind='bar',figsize=(11,5), width=.8, legend ='Inventory')
ax.set_xticklabels(labels,rotation=0)
ax.set_title('Turtle Beach Inventory Day Outstanding', fontsize= 20, x=0.3, y=1.02)
ax.set_xlabel('Source: Turtle Beach Financials; Bloomberg', fontsize =12, x=.8, style = 'italic')
ax.set_ylabel('Total Inventory (Thousands)' )
ax2 = ax.twinx()
ax2.plot(Inv_Days_Out['Inv_Days_Out.'], color = 'orange', label = 'Inventory Days Outstanding', linewidth = 3)
ax2.legend(loc=2)
ax2.set_ylabel('Inventory Days Outstanding (Thousands)')
plt.savefig('Visualizations/Gaming_Visuals/turtle_beach.jpeg', bbox_inches='tight')
