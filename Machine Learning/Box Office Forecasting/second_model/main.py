import numpy as np

def get_data():
    #Get the training and testing data
    return [pd.read_csv('./data/train.csv'), pd.read_csv('./data/test.csv')]

def drop(to_drop, train, test):
    #Drop specified attributes from the training and test data sets
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
        if x<=19:
            return 2000+x
        else:
            return 1900+x
    else:
        return 0

def f(x):
    if x<0:
        return 0
    return x

import pandas as pd

#Get training and test data for all models
train_all, test_all = get_data()
cc_train, cc_test = get_data()
date_train, date_test = get_data()
title_train, title_test = get_data() #Model 4

train_df, test_df = get_data()

# #Train all models on the same training and validation data
training, validation = split_to_validate(train_df, 0.7, 200)

train = training
test = validation
cc_train_s = training
cc_test_s = validation
date_train_s = training
date_test_s = validation
title_train_s = training #Model 4
title_test_s = validation #Model 4

train_df.head()

#ALL ATTRIBUTES
ALL_ATTRIBUTES = ['id','belongs_to_collection','budget','genres','homepage','imdb_id','original_language',
                 'original_title','overview','popularity','poster_path','production_companies',
                 'production_countries','release_date','runtime','spoken_languages', 'status', 'tagline',
                 'title','Keywords','cast','crew','revenue']

to_drop = ['release_date','id','genres','homepage','original_title','title','original_language','overview',
           'production_companies','production_countries','spoken_languages','status','tagline',
           'belongs_to_collection', 'imdb_id','poster_path','Keywords','cast','crew']

train_df, test_df = drop(to_drop, train_df, test_df) #testing
train, test = drop(to_drop, train, test) #training and validation
train_all, test_all = drop(to_drop, train_all, test_all)

#cc_train, cc_test
to_drop1 = ['budget','runtime','popularity','release_date','id','genres','homepage','original_title',
            'title','original_language','overview','production_companies','production_countries',
            'spoken_languages','status','tagline','belongs_to_collection', 'imdb_id','poster_path','Keywords']

cc_train, cc_test = drop(to_drop1, cc_train, cc_test) #testing
cc_train_s, cc_test_s = drop(to_drop1, cc_train_s, cc_test_s) #training and validation

#Count the number of cast members
cc_train_s['cast'] = cc_train_s['cast'].apply(lambda x: x.count('{') if type(x)==str else 0)
cc_test_s['cast'] = cc_test_s['cast'].apply(lambda x: x.count('{') if type(x)==str else 0)
cc_test['cast'] = cc_test['cast'].apply(lambda x: x.count('{') if type(x)==str else 0)

#Count the number of crew members
cc_train_s['crew'] = cc_train_s['crew'].apply(lambda x: x.count('{') if type(x)==str else 0)
cc_test_s['crew'] = cc_test_s['crew'].apply(lambda x: x.count('{') if type(x)==str else 0)
cc_test['crew'] = cc_test['crew'].apply(lambda x: x.count('{') if type(x)==str else 0)

#on all
cc_train['cast'] = cc_train['cast'].apply(lambda x: x.count('{') if type(x)==str else 0)
cc_train['crew'] = cc_train['crew'].apply(lambda x: x.count('{') if type(x)==str else 0)

#date_train, date_test
to_drop2 = ['budget','runtime','popularity','id','genres','homepage','original_title','title','original_language',
            'overview','production_companies','production_countries','spoken_languages','status','tagline',
            'belongs_to_collection', 'imdb_id','poster_path','Keywords','cast','crew']

date_train, date_test = drop(to_drop2, date_train, date_test) #testing
date_train_s, date_test_s = drop(to_drop2, date_train_s, date_test_s) #training and validation

#Get month and year
date_train_s['release_month'] = date_train_s['release_date'].apply(lambda x:int(x.split('/')[0]) if type(x)==str else 0 )
date_train_s['release_year'] = date_train_s['release_date'].apply(lambda x:int(x.split('/')[2])if type(x)==str else 0 )

date_test_s['release_month'] = date_test_s['release_date'].apply(lambda x:int(x.split('/')[0])if type(x)==str else 0 )
date_test_s['release_year'] = date_test_s['release_date'].apply(lambda x:int(x.split('/')[2]) if type(x)==str else 0)

date_test['release_month'] = date_test['release_date'].apply(lambda x:int(x.split('/')[0])if type(x)==str else 0 )
date_test['release_year'] = date_test['release_date'].apply(lambda x:int(x.split('/')[2]) if type(x)==str else 0)

#Convert year
date_train_s['release_year'] = date_train_s['release_date'].apply(ap)
date_test_s['release_year'] = date_test_s['release_date'].apply(ap)
date_test['release_year'] = date_test['release_date'].apply(ap)

#Drop the release_date itself
date_train_s.drop('release_date',axis = 1, inplace = True)
date_test_s.drop('release_date',axis = 1, inplace = True)
date_test.drop('release_date',axis = 1, inplace = True)

#on all
date_train['release_month'] = date_train['release_date'].apply(lambda x:int(x.split('/')[0]) if type(x)==str else 0 )
date_train['release_year'] = date_train['release_date'].apply(lambda x:int(x.split('/')[2]) if type(x)==str else 0 )
date_train['release_year'] = date_train['release_date'].apply(ap)
date_train.drop('release_date', axis = 1, inplace = True)

#MODEL 4
title_train_s = title_train_s[['revenue','title']]
title_train_s['revenue'] = title_train_s['revenue'].apply(np.log)
title_train_s['revenue'] = title_train_s['revenue'].apply(f)

#Full training
title_train = title_train[['revenue','title']]
title_train['revenue'] = title_train['revenue'].apply(np.log)
title_train['revenue'] = title_train['revenue'].apply(f)

#Validation
title_test_s = title_test_s[['revenue','title']]
title_test_s['revenue'] = title_test_s['revenue'].apply(np.log)
title_test_s['revenue'] = title_test_s['revenue'].apply(f)

#Full testing
# title_test = title_test[['revenue','title']]
# title_test['revenue'] = title_test['revenue'].apply(np.log)
# title_test['revenue'] = title_test['revenue'].apply(f)

dictionary = set()
def make_dict(x):
    global dictionary
    x = str(x).split(" ")
    for i in x:
        dictionary.add(i)

title_train_s['title'].apply(make_dict)
title_test_s['title'].apply(make_dict)
#title_test['title'].apply(make_dict)

def set_to_dict(s):
    s = list(s)
    dictionary = dict()
    for i in range(len(s)):
        dictionary[(s[i])] = i
    return dictionary

dictionary = set_to_dict(dictionary)

def create_word_vec(x):
    global dictionary
    x = x.split(" ")
    vec = [0.0]*50
    for i in range(len(x)):
        if x[i] in dictionary:
            vec[i]=dictionary[x[i]]
    return np.array(vec)

title_train_s['title']= title_train_s['title'].apply(create_word_vec)
title_test_s['title']= title_test_s['title'].apply(create_word_vec)
title_train['title'] = title_train['title'].apply(create_word_vec)
#title_test['title'] = title_test['title'].apply(create_word_vec)

train_all.head()

cc_train.head()
date_train.head()

# Print Lengths of training and validation data set

print(len(train_all))
print(len(test_all))
print(len(cc_train))
print(len(cc_test))
print(len(date_train))
print(len(date_test))

#Model 1
trian = train.apply(np.log)
train = train.applymap(f)
train = train.fillna(0)
X = train.drop('revenue', axis=1)
Y = train['revenue']

#for all
train_all = train_all.apply(np.log)
train_all = train_all.applymap(f)
train_all = train_all.fillna(0)
X_0 = train_all.drop('revenue', axis = 1)
Y_0 = train_all['revenue']

test = test.apply(np.log)
test = test.applymap(f)
test = test.fillna(0)
X_test = test.drop('revenue', axis=1)
Y_test = test['revenue']

#Model 2
cc_train_s['revenue'] = cc_train_s['revenue'].apply(np.log)
cc_train_s = cc_train_s.applymap(f)
cc_train_s = cc_train_s.fillna(0)
X1 = cc_train_s.drop('revenue', axis=1)
Y1 = cc_train_s['revenue']

#for all
cc_train['revenue'] = cc_train['revenue'].apply(np.log)
cc_train = cc_train.applymap(f)
cc_train = cc_train.fillna(0)
X_0_1 = cc_train.drop('revenue', axis = 1)
Y_0_1 = cc_train['revenue']

cc_test_s['revenue'] = cc_test_s['revenue'].apply(np.log)
cc_test = cc_test_s.applymap(f)
cc_test_s = cc_test_s.fillna(0)
X1_test = cc_test_s.drop('revenue', axis=1)
Y1_test = cc_test_s['revenue']

#Model 3
date_train_s['revenue'] = date_train_s['revenue'].apply(np.log)
date_train_s = date_train_s.applymap(f)
date_train_s = date_train_s.fillna(0)
X2 = date_train_s.drop('revenue', axis = 1)
Y2 = date_train_s['revenue']

# for all
date_train['revenue'] = date_train['revenue'].apply(np.log)
date_train = date_train.applymap(f)
date_train = date_train.fillna(0)
X_0_2 = date_train.drop('revenue', axis=1)
Y_0_2 = date_train['revenue']

date_test_s['revenue'] = date_test_s['revenue'].apply(np.log)
date_test_s = date_test_s.applymap(f)
date_test_s = date_test_s.fillna(0)
X2_test = date_test_s.drop('revenue', axis = 1)

#Model 4
#title_train_s = training
#title_test_s = validation
X3 = title_train_s['title']
X3 = np.stack(X3.to_numpy(), axis = 0)

Y3 = title_train_s['revenue']
X3_test = title_test_s['title']
Y3_test = title_test_s['revenue']
X3_test = np.stack(X3_test.to_numpy(), axis=0)

#for all
X_0_3 = title_train['title']
X_0_3 = np.stack(X_0_3.to_numpy(), axis = 0)
Y_0_3 = title_train['revenue']

#Model 1
train_all.head()

from keras import models, layers, regularizers, optimizers

def model1(X, Y, X_test, Y_test):
    model1 = models.Sequential()
    model1.add(layers.Dense(356, activation='relu', input_shape=(X.shape[1],)))
    model1.add(layers.Dropout(0.1))
    model1.add(layers.Dense(256, activation='relu'))
    model1.add(layers.Dense(10,activation='relu'))
    model1.add(layers.Dense(1))

    model1.compile(optimizer=optimizers.rmsprop(lr=1e-5),loss='mse',metrics=['mean_squared_logarithmic_error'])
    #history = model1.fit(X,Y,epochs=40, batch_size = 32, validation_data=(X_test, Y_test))
    history = model1.fit(X, Y, epochs = 40, batch_size = 32)
    return [model1, history]

def model2(X1, Y1, X1_test, Y1_test):
    model2 = models.Sequential()
    model2.add(layers.Dense(356, activation='relu', input_shape=(X1.shape[1],)))
    model2.add(layers.Dropout(0.2))
    model2.add(layers.BatchNormalization())
    model2.add(layers.Dense(256, activation='relu'))
    model2.add(layers.Dropout(0.2))
    model2.add(layers.Dense(128, activation='relu'))
    model2.add(layers.Dropout(0.2))
    model2.add(layers.Dense(64, activation='relu')) #Added
    model2.add(layers.Dropout(0.2)) #Added
    model2.add(layers.Dense(10,activation='relu'))
    model2.add(layers.Dense(1))

    model2.compile(optimizer=optimizers.rmsprop(lr=1e-5),loss='msle',metrics=['mean_squared_logarithmic_error'])
    #history = model2.fit(X1, Y1, epochs=50, batch_size = 32, validation_data=(X1_test, Y1_test))
    history = model2.fit(X1, Y1, epochs = 50, batch_size = 32)
    return [model2, history]

def model3(X2, Y2, X2_test, Y2_test):
    model3 = models.Sequential()
    model3.add(layers.Dense(356, activation='relu', input_shape=(X2.shape[1],)))
    model3.add(layers.Dropout(0.2))
    model3.add(layers.Dense(256, activation='relu'))
    model3.add(layers.Dense(10,activation='relu'))
    model3.add(layers.Dense(1))

    model3.compile(optimizer=optimizers.rmsprop(lr=1e-5),loss='mse',metrics=['mean_squared_logarithmic_error'])
    #history = model3.fit(X2, Y2, epochs=40, batch_size = 32, validation_data=(X2_test, Y2_test))
    history = model3.fit(X2, Y2, epochs = 50, batch_size = 32)

    return [model3, history]

model1, history1 = model1(X_0, Y_0, X_test, Y_test)
model1.summary()
