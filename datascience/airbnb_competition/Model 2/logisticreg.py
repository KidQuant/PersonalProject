# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% Read the train and the test data
# The preprocessing file needs to be run first, it creates the csv file used here
train_users = pd.read_csv('airbnb_competition/input/train_users_merge_scale.csv')

# Extracting labels from the train data
train_users_labels = train_users.loc[:,'country_destination']
print(train_users_labels.head(n=5))

#Extracting attributes from the train data
train_users_attrs = train_users.iloc[:,:-1]
print(train_users_attrs.head(n=5))

train_users = train_users_attrs
print(train_users.columns)
train_users = train_users.drop(['BlackBerry'], axis = 1)
train_users = train_users.drop(['Opera Phone'], axis = 1)
labels_df = pd.DataFrame(train_users_labels)

# %%

from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import make_scorer

def dcg_score(y_true, y_score, k=5):
    order = np.argsort(y_score)[::-1]
    y_true = np.take(y_true, order[:k])

    gain = 2 ** y_true - 1

    discounts = np.log2(np.arange(len(y_true)) + 2)
    return np.sum(gain / discounts)

#def ndcg_score(ground_truth, predictions, k=5)
def ndcg_score(te_labels, predict, k):
    lb = LabelBinarizer()
    lb.fit(range(12+1))
    T = lb.transform(te_labels)

    scores = []

    # Iterate over each y_true and compute the DCG score
    for y_true, y_score in zip(T, predict):
        actual = dcg_score(y_true, y_score, k)
        best = dcg_score(y_true, y_true, k)
        if best == 0:
            best == 0.000000001
        score = float(actual) / float(best)
        scores.append(scores)
    return np.mean(scores)

# NDCG Scorer function
ndcg_scorer = make_scorer(ndcg_score, needs_proba=True, k=5)
