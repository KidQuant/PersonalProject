import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from nltk.corpus import stopwords
from collections import Counter
import nltk
%matplotlib inline
sns.set(style = 'whitegrid', palette = 'muted', font_scale=1.3)

df = pd.read_csv('andres_rejections.csv')
df.head()

df.info()

df['Subject'].value_counts()
