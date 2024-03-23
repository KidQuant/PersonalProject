
# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.image as image
from PIL import Image

plt.style.use('dark_background')


image = Image.open("download.png")

fig, ax = plt.subplots(figsize=(10,7))

values = [100]
colors = ['b']
labels = ['Sell']
plt.pie(values, colors=colors, labels= values,counterclock=False, shadow=True)
ax.legend(labels)
ax.grid(linestyle='-', linewidth='0.5', color='red')
ax.set_title("What's Clin Favorite Thing To Do In Warzone?")

plt.show()
