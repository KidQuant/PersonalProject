import gc
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.sparse import csr_matrix, hstack
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
import lightgbm as lgb

df = pd.read_csv('mercari/train.tsv', sep ='\t')

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

train.shape, test.shape

train.head()

train.info()

train.price.describe()

plt.subplot(1,2,1)
(train['price']).plot.hist(bins=50, figsize=(12,6), edgecolor = 'white', range = [0,250])
plt.xlabel('Price', fontsize=12)
plt.title('Price Distribution', fontsize=12)

plt.subplot(1,2,2)
np.log(train['price']+1).plot.hist(bins=50, figsize=(12,6), edgecolor ='white')
plt.xlabel('log(price+1)', fontsize=12)
plt.ylabel('Price Distribution', fontsize = 12)

train['shipping'].value_counts() / len(train)

shipping_fee_by_buyer = train.loc[df['shipping'] == 0, 'price']
shipping_fee_by_seller = train.loc[df['shipping'] == 1, 'price']

fig, ax = plt.subplots(figsize = (18,8))
ax.hist(shipping_fee_by_seller, color = '#8CB4E1', alpha = 1.0, bins = 50, range = [0,100], label = 'Price when Seller pays Shipping')
ax.hist(shipping_fee_by_buyer, color='#007D00', alpha = 0.7, bins = 50, range = [0,100], label = 'Price when Buyer pays Shipping')
plt.xlabel('Price', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Price Distribution by Shipping Type', fontsize = 15)
plt.legend()
plt.show()

print('The average price is {}'.format(round(shipping_fee_by_seller.mean(),2)), 'if seller pays shipping');
print('The average price is {}'.format(round(shipping_fee_by_buyer.mean(),2)), 'if buyer pays shipping')

fig, ax = plt.subplots(figsize = (18,8))
ax.hist(np.log(shipping_fee_by_seller+1), color = '#8CB4E1', alpha = 1.0, bins = 50, label = 'Price when Seller pay Shipping')
ax.hist(np.log(shipping_fee_by_buyer+1), color = '#007D00', alpha = 0.7, bins = 50, label = 'Price when Buyer pays Shipping')
plt.xlabel('log(price+1)', fontsize = 12)
plt.ylabel('frequency', fontsize = 12)
plt.tick_params(labelsize=12)
plt.legend()
plt.show()

print('There are', train['category_name'].nunique(), 'unique values in category name column')

train['category_name'].value_counts()[:10]

sns.boxplot(x = 'item_condition_id', y = np.log(train['price']+1),
data = train, palette = sns.color_palette('RdBu',5))

NUM_BRANDS = 4000
NUM_CATEGORIES = 1000
NAME_MIN_DF = 10
MAX_FEATURES_ITEM_DESCRIPTION = 50000

print('There are %d items that do not have a category name.'
%train['category_name'].isnull().sum())

print('There are %d items that do not have a description.'
%train['item_description'].isnull().sum())

def handle_missing_inplace(dataset):
    dataset['category_name'].fillna(value = 'missing', inplace=True)
    dataset['brand_name'].fillna(value = 'missing', inplace = True)
    dataset['item_description'].replace('No description yet,''missing', inplace=True)
    dataset['item_description'].fillna(value='missing', inplace=True)

def cutting(dataset):
    pop_brand = dataset['brand_name'].value_counts().loc[lambda x: x.index != 'missing'].index[:NUM_BRANDS]
    dataset.loc[~dataset['brand_name'].isin(pop_brand), 'brand_name'] = 'missing'
    pop_category = dataset['category_name'].value_counts().loc[lambda x: x.index != 'missing'].index[:NUM_CATEGORIES]

def to_categorical(dataset):
    dataset['category_name'] = dataset['category_name'].astype('category')
    dataset['brand_name'] = dataset['brand_name'].astype('category')
    dataset['item_condition_id'] = dataset['item_condition_id'].astype('category')

df = pd.read_csv('mercari/train.tsv', sep = '\t')
msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[msk]
test_new = test.drop('price', axis =1)
y_test = np.log1p(test['price'])

train = train[train.price != 0].reset_index(drop=True)

nrow_train = train.shape[0]
y = np.log1p(train['price'])
merge: pd.DataFrame = pd.concat([train, test_new])

handle_missing_inplace(merge)
cutting(merge)
to_categorical(merge)

cv = CountVectorizer(min_df = NAME_MIN_DF)
X_name = cv.fit_transform(merge['name'])

cv = CountVectorizer()
X_category = cv.fit_transform(merge['category_name'])

tv = TfidfVectorizer(max_features=MAX_FEATURES_ITEM_DESCRIPTION, ngram_range=(1,3), stop_words = 'english')
X_description = tv.fit_transform(merge['item_description'])