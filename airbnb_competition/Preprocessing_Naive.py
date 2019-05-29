
# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% Read the train and the test data
train_users = pd.read_csv('airbnb_competition/input/train_users_2.csv')
test_users = pd.read_csv('airbnb_competition/input/test_users.csv')

# Extracting labels from the train data
train_users_labels = train_users.loc[:,'country_destination']
print(train_users_labels.head(n=5))

# Extracting attributes from the train data
train_users_attrs = train_users.iloc[:, 0:15]
print(train_users_attrs.head(n=5))

train_users = train_users_attrs

train_users = train_users.drop(['date_first_booking'], axis =1)
test_users = test_users.drop(['date_first_booking'], axis=1)

# %% Date is split into 3 parts as year, month, and day in both test and train. These are added
# new features in both test and train

date_acc_created = np.vstack(train_users.date_account_created.astype(str).apply(lambda x: list(map(int, x.split('-')))).values)
train_users['created_year'] = date_acc_created[:,0]
train_users['created_month'] = date_acc_created[:,1]
train_users['created_day'] = date_acc_created[:,2]
train_users = train_users.drop(['date_account_created'], axis=1)

date_acc_created_test = np.vstack(test_users.date_account_created.astype(str).apply(lambda x: list(map(int, x.split('-')))).values)
test_users['created_year'] = date_acc_created_test[:,0]
test_users['created_month'] = date_acc_created_test[:,1]
test_users['created_day'] = date_acc_created_test[:,2]
test_users = test_users.drop(['date_account_created'], axis=1)

# %% Replacing unknown values in gender with -1 and null values with -1
train_users.loc[ train_users['gender'] == '-unknown-', 'gender'] = -1
train_users.loc[ train_users['gender'].isnull(), 'gender'] = -1
test_users.loc[ test_users['gender'] == '-unknown-', 'gender'] = -1
test_users.loc[ test_users['gender'].isnull(), 'gender'] = -1

# Encoding Female with 0, Male with 1 and Other with 2 in both test and train data
gender_translation = {'FEMALE' : 0,
                      'MALE' : 1,
                      'OTHER' : 2,
                      -1 : -1 }
for data in [train_users, test_users]:
    data['gender'] = data['gender'].apply(lambda x: gender_translation[x])

# Finding valid values for gender and invalid values for gender
nan_gender_count = len(train_users.loc[train_users['gender'] == -1, 'gender'])
valid_gender_count = len(train_users.gender.values) - nan_gender_count

# Creating a map with the gender distribution
count_map = pd.value_counts(train_users['gender'].values)
print('Existing gender value distribution')
for k, v in count_map.iteritems():
    if k == -1:
        continue
    print(k, ':', float(v)/float(valid_gender_count))


# %% Making the gender distribution the same for missing imputation
for k, v in count_map.iteritems():
    if k == -1:
        continue
    c = int( nan_gender_count * float(v)/float(valid_gender_count))
    for i in range(len(train_users.gender.values)):
        if train_users.gender.values[i] == -1:
            train_users.gender.values[i] = k
            c -= 1
        if c == 0:
            break
train_users.gender.values[213450] = 0

train_users.gender.describe()

nan_gender_count = len(test_users.loc[test_users['gender'] == -1, 'gender'])
valid_gender_count = len(test_users.gender.values) - nan_gender_count
count_map = pd.value_counts(test_users['gender'].values)
print ("Existing gender value distribution")
for k, v in count_map.iteritems():
    if k == -1:
        continue
    print (k, ":", float(v)/float(valid_gender_count))

for k, v in count_map.iteritems():
    if k == -1:
        continue
    c = int ( nan_gender_count * float(v)/float(valid_gender_count) )
    for i in range(len(test_users.gender.values)):
        if test_users.gender.values[i] == -1:
            test_users.gender.values[i] = k
            c -= 1
        if c == 0:
            break
test_users.gender.values[62094] = 0

train_users['age'].describe()

# %% Replacing invalid age with NaN in test and training set

train_users.loc[train_users['age'] > 95, 'age'] = np.nan
train_users.loc[train_users['age'] < 16, 'age'] = np.nan
test_users.loc[test_users['age'] > 95, 'age'] = np.nan
test_users.loc[test_users['age'] < 16, 'age'] = np.nan

# Replace missing age with median
print(train_users.age.median())
print(test_users.age.median())
train_users.loc[ train_users['age'].isnull(), 'age'] = train_users.age.median()
test_users.loc[ test_users['age'].isnull(), 'age'] = test_users.age.median()

# %%  Encoding the signup method for test
signup_translation = {'facebook' : 0,
                     'google' : 1,
                     'basic' : 2,
                     'weibo' : 3}
for data in [train_users, test_users]:
    data['signup_method'] = data['signup_method'].apply(lambda x: signup_translation[x])

# Encoding the language in both train and test
test_users.loc[ test_users['language'] == '-unknown-', 'language'] = "en"

# Encoding the language in both train and test
language_encoding = {'en'      :       1       ,
'zh'      :       2       ,
'fr'      :       3       ,
'es'      :       4       ,
'ko'      :       5       ,
'de'      :       6       ,
'it'      :       7       ,
'ru'      :       8       ,
'pt'      :       9       ,
'ja'      :       10      ,
'sv'      :       11      ,
'nl'      :       12      ,
'tr'      :       13      ,
'da'      :       14      ,
'pl'      :       15      ,
'cs'      :       16      ,
'no'      :       17      ,
'el'      :       18      ,
'th'      :       19      ,
'id'      :       20      ,
'hu'      :       21      ,
'fi'      :       22      ,
'ca'      :       23      ,
'is'      :       24      ,
'hr'      :       25}

for data in [train_users, test_users]:
    data['language'] = data['language'].apply(lambda x: language_encoding[x])

# Encoding for affiliate_channel

affiliate_channel_encoding = {'direct' : 1,
                             'sem-brand' : 2,
                             'sem-non-brand' : 3,
                             'other' : 4,
                             'api' : 5,
                             'seo' : 6,
                             'content' : 7,
                             'remarketing' : 8}
for data in [train_users, test_users]:
    data['affiliate_channel'] = data['affiliate_channel'].apply(lambda x: affiliate_channel_encoding[x])


# Encoding for affiliate_provider
affiliate_provider_encoding = {'direct':1,
'google':2,
'other':3,
'craigslist':4,
'bing':5,
'facebook':6,
'vast':7,
'padmapper':8,
'facebook-open-graph':9,
'yahoo':10,
'gsp':11,
'meetup':12,
'email-marketing':13,
'naver':14,
'baidu':15,
'yandex':16,
'wayn':17,
'daum':18}

for data in [train_users, test_users]:
    data['affiliate_provider'] = data['affiliate_provider'].apply(lambda x: affiliate_provider_encoding[x])

train_users.loc[ train_users['first_affiliate_tracked'].isnull(), 'first_affiliate_tracked'] = 'untracked'
test_users.loc[ test_users['first_affiliate_tracked'].isnull(), 'first_affiliate_tracked'] = 'untracked'
first_affiliate_tracked_encoding = {'untracked': 1,
                                    'linked' : 2,
                                    'omg' : 3,
                                    'tracked-other' : 4,
                                    'product' : 5,
                                    'marketing' : 6,
                                    'local ops' : 7}

for data in [train_users, test_users]:
    data['first_affiliate_tracked'] = data['first_affiliate_tracked'].apply(lambda x: first_affiliate_tracked_encoding[x])

# Encoding for signup_app
# Encoding for signup_app
signup_app_encoding = {'Web' : 1,
                      'iOS' : 2,
                      'Android' : 3,
                      'Moweb' : 4}
for data in [train_users, test_users]:
    data['signup_app'] = data['signup_app'].apply(lambda x: signup_app_encoding[x])

# Encoding for first_device_type
# Encoding for first_device_type
first_device_type_encoding = { 'Mac Desktop' : 1,
                             'iPhone' : 2,
                             'Windows Desktop' : 3,
                             'Android Phone' : 4,
                             'iPad' : 5,
                             'Android Tablet' : 6,
                             'Other/Unknown' : 7,
                             'Desktop (Other)' : 8,
                             'SmartPhone (Other)' : 9}

for data in [train_users, test_users]:
    data['first_device_type'] = data['first_device_type'].apply(lambda x: first_device_type_encoding[x])

# Encoding for first_browser
first_browser_encoding = {'Chrome':1,
'Safari':2,
'Firefox':3,
'-unknown-':4,
'IE':5,
'Mobile Safari':6,
'Chrome Mobile':7,
'Android Browser':8,
'AOL Explorer':9,
'Opera':10,
'Silk':11,
'Chromium':12,
'BlackBerry Browser':13,
'Maxthon':14,
'IE Mobile':15,
'Apple Mail':16,
'Sogou Explorer':17,
'Mobile Firefox':18,
'RockMelt':19,
'SiteKiosk':20,
'Iron':21,
'IceWeasel':22,
'Pale Moon':23,
'SeaMonkey':24,
'Yandex.Browser':25,
'CometBird':26,
'Camino':27,
'TenFourFox':28,
'wOSBrowser':29,
'CoolNovo':30,
'Avant Browser':31,
'Opera Mini':32,
'Mozilla':33,
'Comodo Dragon':34,
'TheWorld Browser':35,
'Crazy Browser':36,
'Flock':37,
'OmniWeb':38,
'SlimBrowser':39,
'Opera Mobile':40,
'Conkeror':41,
'Outlook 2007':42,
'Palm Pre web browser':43,
'Stainless':44,
'NetNewsWire':45,
'Kindle Browser':46,
'Epic':47,
'Googlebot':48,
'Arora':49,
'Google Earth':50,
'IceDragon':51,
'PS Vita browser':52,
'IBrowse' : 53,
'UC Browser' : 54,
'IBrowse': 55,
'Nintendo Browser' : 56}

for data in [train_users, test_users]:
    data['first_browser'] = data['first_browser'].apply(lambda x: first_browser_encoding[x])

# %% Reading sessions data
sessions = pd.read_csv('airbnb_competition/input/sessions.csv')

df = sessions['user_id'].value_counts()
print(df.shape)
print(df)

train_users['session_count'] = 0

for key, val in df.iteritems():
    train_users.loc[train_users['id'] == key, 'session_count'] = val

print(train_users['session_count'].max())



#Encoding for country_destination
country_destination_encoding = {'NDF': 0,
'US' : 1,
'other' : 2,
'FR' : 3,
'IT' : 4,
'GB' : 5,
'ES' : 6,
'CA' : 7,
'DE' : 8,
'NL' : 9,
'AU' : 10,
'PT' : 11}

labels_df = train_users_labels.to_frame()

for data in [labels_df]:
    data['country_destination'] = data['country_destination'].apply(lambda x: country_destination_encoding[x])



from sklearn import preprocessing

stdscaler = preprocessing.StandardScaler()
train_users_scaled = stdscaler.fit_transform(train_users.values)
train_users = pd.DataFrame(train_users_scaled, columns = train_users.columns)

train_users_merge_scaled = stdscaler.fit_transform(train_users_merge.values);
train_users_merge = pd.DataFrame(train_users_merge_scaled, columns = train_users_merge.columns)

test_users_scaled = stdscaler.fit_transform(test_users.values)
#test_users = pd.DataFrame(test_users_scaled, columns = test_users.columns)

"""
train_users['country_destination'] = labels_df
print(train_users.head())

train_users_merge['country_destination'] = labels_df
#print(train_users_merge.head())

#train_users.to_csv('train_users_wo_merge_scale.csv',index=False)
#train_users_merge.to_csv('train_users_merge_scale.csv',index=False)

#train_users_merge_wo_scale['country_destination'] = labels_df
#train_users_merge_wo_scale.to_csv('train_users_merge_wo_scale.csv',index=False)
#test_users_merge_wo_scale.to_csv('test_users_merge_wo_scale.csv',index=False)

#train_user_wo_merge_wo_scale['country_destination'] = labels_df
#train_user_wo_merge_wo_scale.to_csv('train_users_wo_merge_wo_scale.csv',index=False)
#test_user_wo_merge_wo_scale.to_csv('test_users_wo_merge_wo_scale.csv',index=False)

def folds_to_split(data,targets,train,test):
    data_tr = pd.DataFrame(data).iloc[train]
    data_te = pd.DataFrame(data).iloc[test]
    labels_tr = pd.DataFrame(targets).iloc[train]
    labels_te = pd.DataFrame(targets).iloc[test]
    return [data_tr, data_te, labels_tr, labels_te]


# %% Creating the NDCG Scorer

from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import make_scorer

def dcg_score(y_true, y_score, k=5):
    order = np.argsort(y_score)[::-1]
    y_true = np.take(y_true, order[:k])

    gain = 2 ** y_true - 1

    discounts = np.log2(np.arange(len(y_true)) + 2)
    return np.sum(gain / discounts)


#def ndcg_score(ground_truth, predictions, k=5):
def ndcg_score(te_labels, predict, k):

    lb = LabelBinarizer()
    lb.fit(range(len(predict) + 1))
    T = lb.transform(te_labels)

    scores = []

    # Iterate over each y_true and compute the DCG score
    for y_true, y_score in zip(T, predict):
        actual = dcg_score(y_true, y_score, k)
        best = dcg_score(y_true, y_true, k)
        if best == 0:
            best = 0.000000001
        score = float(actual) / float(best)
        scores.append(score)
    return np.mean(scores)


# NDCG Scorer function
ndcg_scorer = make_scorer(ndcg_score, needs_proba=True, k=5)
print(ndcg_scorer)

#print train_users.head()
train_users = train_users.drop(['id'], axis = 1)
#print train_users.head()

# %% Modeling

from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

gnb = GaussianNB()
[tr_data, te_data, tr_labels, te_labels] = train_test_split(train_users, labels_df, test_size=0.33,random_state=20160302)
gnb.fit(tr_data, tr_labels.values.ravel())

prob_arr = gnb.predict_proba(te_data)

ground_truth = te_labels.as_matrix()
predictions = prob_arr
score = ndcg_score(ground_truth, predictions, k=5)
print(score)

print('NDCG Score for Naive Bayes')
print(score)

# %% Native Bayes with 10-fold cross-validation

foldnum = 0
fold_results = pd.DataFrame()
for train, test in cross_validation.KFold(len(train_user), n_folds=10, random_state=20160302,shuffle=True):
    foldnum+=1
    [tr_data, te_data, tr_labels, te_labels] = folds_to_split(train_users, labels_df, train,test)
    gnb1 = GaussianNB()
    gnb1.fit(tr_data, tr_labels, tr_labels.values.ravel())
    prob_arr_gnb1 = gnb1.predict_proba(te_data)
    #ground_truth = te_Labels.as_matrix()
    #fold_results.Loc[foldnum, 'Accuracy'] = gnb.score(te_data, te_Labels)
    score_gnb1 = ndcg_score(te_labels.as_matrix(), prob_arr_gnb1, k=5)
    fold_results.loc[foldnum, 'Ndcg_Gnb'] = score_gnb1

print(fold_results.mean())

from sklearn import preprocessing
train_users_scaled = pd.DataFrame(preprocessing.StandardScaler().fit_transform(train_users))
print(train_users_scaled.head(n=5))

foldnum = 0
fold_results = pd.DataFrame()
for train, test in cross_validation.KFold(len(train_users_scaled), n_fold=10, random_state=20160302, shuffle=True):
    foldnum+=1
    [tr_data, te_data, tr_labels, te_labels] = folds_to_split(train_users_scaled,label_df,train, test)
    gnb2 = GaussianNB()
    gnb2.fit(tr_data, tr_labels.values.ravel())
    prob_arr_gnb2 = gnb2.predict_proba(te_data)
    #ground_truth = te_labels.as_matrix()
    #fold_results.loc[foldnum, 'Accuracy'] = gnb.score(te_data, te_labels)
    score_gnb2 = ndcg_score(te_labels.as_matrix(), prob_arr_gnb2, k=5)
    fold_results.loc[foldnum, 'Ndcg_Gnb'] = score_gnb2

print(fold_results.mean())
