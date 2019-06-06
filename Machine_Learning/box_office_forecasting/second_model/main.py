import numpy as np
def get_data():
    #Get the training data and testing data
    return [pd.read_csv('./data/train.csv'), pd.read_csv('./data/test.csv')]

def drop(to_drop, train, test):
    #Drop specified attributes from teh traiing and test data sets
    for x in to_drop:
        try:
            train = train.drop(x, axis = 1)
            if x != 'revenue':
                test = test.drop(x, axis = 1)
        except:
            pass
    return [train, test]

def split_to_validate(train, fraction, random):
    #Split training data into training and validation data
    ret_train = train.sample(frac=fraction, random_state=random)
    ret_test = train.drop(ret_train.index)
    return [ret_train, ret_test]

def ap(x):
    #Convert years (ex: 86 -> 1986, 15 -> 2015)
    if type(x) == str:
        x = int(x.split('/')[2])
        if x <= 19:
            return 2000+x
        else:
            return 1900+x
    else:
        return 0

def f(x):
    if x < 0:
        return 0
    return x

import pandas as pd

#Get training and test data for all models
train_all, test_all = get_data()
cc_train, cc_test = get_data()
date_train, date_test = get_data()
title_train, title_test = get_data()

train_df, test_df = get_data()

# #Train all model on the dame training and validation data
training, validation = split_to_validate(train_df, 0.7,200)

train = training
test = validation
cc_train_s = training
cc_test_s = validation
date_train_s = training
date_test_s =  validation
title_train_s = training #model4
title_test_s = validation #model4

train_df.head()

train_all.info()

#ALL ATRRIBUTE
ALL_ATTRIBUTES = ['id', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'imdb_id', 'original_language',
'original_title', 'overview', 'popularity', 'poster_path', 'production_companies', 'production_countries',
'release_date', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'Keywords', 'cast', 'crew', 'revenue']

to_drop = ['release_date', 'id', 'genre', 'homepage', 'original_title', 'title', 'original_language', 'overview',
'production_companies', 'production_countries', 'spoken_languages', 'status', 'tagline', 'belongs_to_collection',
'imdb_id', 'poster_path', 'Keywords', 'cast', 'crew']

train_df, test_df = drop(to_drop, train_df, test_df)
train_df, test = drop(to_drop, train, test) #training and validation
train_all, test_all = drop(to_drop, train_all, test_all)

#cc_train, cc_test
to_drop1 = ['budget', 'runtime', 'popularity', 'release_date', 'id', 'genres', 'homepage', 'original_title',
'title', 'original_language', 'overview', 'production_companies', 'production_countries', 'spoken_languages',
'status','tagline', 'belongs_to_collection', 'imdb_id', 'poster_path', 'Keywords']

cc_train, cc_test = drop(to_drop1, cc_train, cc_test)
cc_train_s, cc_test_s = drop(to_drop1, cc_train_s, cc_test_s)

#count the number of cast members
cc_train_s['cast'] = cc_train_s['cast'].apply(lambda x: x.count('{') if type(x) == str else 0)
cc_test_s['cast'] = cc_test_s['cast'].apply(lambda x: x.count('{') if type(x) == str else 0)
cc_test['cast'] = cc_test['cast'].apply(lambda x: x.count('{') if type(x) == str else 0)

#Count the number of crew members
cc_test_s['crew'] = cc_test_s['crew'].apply(lambda x: x.count('{') if type(x) == str else 0)
cc_test_s['crew'] = cc_test_s['crew'].apply(lambda x: x.count('{') if type(x) == str else 0)
cc_test['crew'] = cc_test['crew'].apply(lambda x: x.count('{') if type(x) == str else 0)

#on all
cc_train['cast'] = cc_train['cast'].apply(lambda x: x.count('{') if type(x) == str else 0)
cc_train['crew'] = cc_train['cast'].apply(lambda x: x.count('{') if type(x) == str else 0 )

#date_train, date_test
to_drop2 = ['budget', 'runtime', 'popularity', 'id', 'genres', 'homepage', 'original_title', 'title',
'original_language', 'overview', 'production_companies', 'production_countries', 'spoken_languages',
'status', 'tagline', 'belongs_to_collection', 'imdb_id', 'poster_path', 'Keywords', 'cast', 'crew']

date_train, date_test = drop(to_drop2, date_train, date_test) #testing
date_train_s, date_test_s = drop(to_drop2, date_train_s, date_test_s) #training and validation

#Get month and year
date_train_s['release_month'] = date_train_s['release_date'].apply(lambda x:int(x.split('/')
[0]) if type(x) == str else 0)
date_test_s['release_year'] = date_test_s['release_date'].apply(lambda x:int(x.split('/')
[2]) if type(x) == str else 0)

date_test_s['release_month'] = date_test_s['release_date'].apply(lambda x: int(x.split('/')
[0]) if type(x) == str else 0)
date_test['release_year'] = date_test['release_date'].apply(lambda x: int(x.split('/')[2])
if type(x) == str else 0)

#Convert year
date_train_s['release_year'] = date_train_s['release_date'].apply(ap)
date_test_s['release_year'] = date_test_s['release_date'].apply(ap)
date_test['release_year'] = date_test['release_date'].apply(ap)

#Drop the release_date itself
date_train_s.drop('release_date', axis=1, inplace=True)
date_test_s.drop('release_date', axis=1, inplace=True)
date_test.drop('release_date', axis=1, inplace=True)

#on all
date_train['release_month'] = date_train['release_date'].apply(lambda x:int(x.split('/')[0])
if type(x) == str else 0)
date_train['release_year'] = date_train['release_date'].apply(lambda x: int(x.split('/')[2])
if type(x) == str else 0)
date_train['release_year'] = date_train['release_date'].apply(ap)
date_train.drop('release_date', axis =1, inplace=True)

#MODEL 4
title_train_s = title_train_s[['revenue', 'title']]
title_train_s['revenue'] = title_train_s['revenue'].apply(np.log)
title_train_s['revenue'] = title_train_s['revenue'].apply(f)

#Full training
title_train = title_train[['revenue', 'title']]
title_train['revenue'] = title_train['revenue'].apply(np.log)
title_train['revenue'] = title_train['revenue'].apply(f)

#Validation
title_test_s = title_test_s[['revenue', 'title']]
title_test_s['revenue'] = title_test_s['revenue'].apply(np.log)
title_test_s['revenue'] = title_test_s['revenue'].apply(f)

#Full testing
# title_test = title_test[['revenue','title']]
# title_test['revenue'] = title_test['revenue'].apply(np.log)
# title_test['revenue'] = title_test['revenue'].apply(f)
