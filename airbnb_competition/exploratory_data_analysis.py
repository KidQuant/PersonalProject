import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.model_selection import train_test_split

from subprocess import check_output
print(check_output(["ls", "input"]).decode("utf8"))


# data from csv files is imported to pandas data frames
data_train_org = pd.read_csv("input/train_users_2.csv")
print(data_train_org.columns)
data_train_org = data_train_org.sort_values(by='timestamp_first_active')
print(data_train_org.shape)

data_train, data_test = train_test_split(data_train_org, test_size = 0.2)
data_train_copy = data_train
print('%d items in training data, %d in test data' % (len(data_train), len(data_test)))

# Removing the data_first_booking column from data_train, data_test
print(data_train.columns)
