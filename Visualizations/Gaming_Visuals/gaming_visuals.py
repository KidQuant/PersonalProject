import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gaming_trends = pd.DataFrame({'Average MAU': [65, 140, 190, 225, 260, 295,335,360],
                              'Mobile Average MAU': [25, 70, 135, 185, 225, 248, 265, 330]},
                              index = ['2015A','2016A','2017A','2018E','2019E','2020E','2021E','2022E'])

gaming_trends.plot(kind='bar', figsize = (11,5), ylim = (0, 500))
plt.title('China Live Game Streaming MAU Forecast', x=.3, y=1.02, fontsize=20)
plt.ylabel('In Millions', fontsize = 12)
plt.xticks(rotation =0)
plt.xlabel('Source: Huya F-1; Bloomberg', x=0.9,style='italic')
plt.savefig('Visualizations/Gaming_Visuals/gaming_trends.jpeg', bbox_inches='tight')


headset_trends = pd.DataFrame({'Gaming Peripheral': [1.5, 2.3, 2.9, 3.3, 4.2, 4.6, 5.9]},
                              index = ['2014A','2015A','2016A','2017A','2018E','2020E','2021E'])

headset_trends.plot(kind = 'bar', figsize=(11,5))
