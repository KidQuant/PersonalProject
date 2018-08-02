import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

df = pd.read_csv('train.csv.gz', sep=',').dropna()
df = df.sample(frac=0.01, random_state=99)

df.shape

count_classes = pd.value_counts(df['is_booking'], sort = True).sort_index()

count_classes.plot(kind = 'bar')
plt.title('Booking or Not booking')
plt.xlabel('Class')
plt.ylabel('Frequency')
