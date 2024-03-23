import pandas as pd

train_df = pd.read_csv('./data/train.csv')
test_df = pd.read_csv('./data/test.csv')
train_df.head()

to_drop = ['id', 'belongs_to_collection', 'homepage', 'imdb_id', 'original_title', 'title', 'original_language',
'overview', 'poster_path', 'status', 'tagline', 'Keywords']
for x in to_drop:
    train_df = train_df.drop(x, axis=1)
    if x != 'revenue':
        test_df =test_df.drop(x,axis=1)


train_df['spoken_languages'] = train_df['spoken_languages'].apply(lambda x: x.count('{') if type(x)==str else 0)
test_df['spoken_languages'] = test_df['spoken_languages'].apply(lambda x: x.count('{') if type(x)==str else 0)
train_df['production_companies'] =train_df['production_companies'].apply(lambda x: x.count('{') if type(x)==str else 0)
test_df['production_companies'] = test_df['production_companies'].apply(lambda x: x.count('{') if type(x)==str else 0)
train_df['production_countries'] =train_df['production_countries'].apply(lambda x: x.count('{') if type(x)==str else 0)
test_df ['production_countries']= test_df['production_countries'].apply(lambda x: x.count('{') if type(x)==str else 0)
train_df['cast'] =train_df['cast'].apply(lambda x: x.count('{') if type(x)==str else 0)
test_df['cast'] = test_df['cast'].apply(lambda x: x.count('{') if type(x)==str else 0)
train_df['crew'] =train_df['crew'].apply(lambda x: x.count('{') if type(x)==str else 0)
test_df['crew'] = test_df['crew'].apply(lambda x: x.count('{') if type(x)==str else 0)
train_df['genres'] =train_df['genres'].apply(lambda x: x.count('{') if type(x)==str else 0)
test_df ['genres']= test_df['genres'].apply(lambda x: x.count('{') if type(x)==str else 0)

def ap(x):
    if type(x) == str:
        n = int(x.split('/')[2])
        if(n<=19):
            return 2000+n
        else:
            return 1900+n
    else:
        return 0

train_df['release_month'] = train_df['release_date'].apply(lambda x:int(x.split('/')[0]) if type(x)==str else 0 )
train_df['release_year'] = train_df['release_date'].apply(ap)
train_df['release_date'] = train_df['release_date'].apply(lambda x:int(x.split('/')[1])if type(x)==str else 0 )
test_df['release_month'] = train_df['release_date'].apply(lambda x:int(x.split('/')[0])if type(x)==str else 0 )
test_df['release_year'] = train_df['release_date'].apply(ap)
test_df['release_date'] = train_df['release_date'].apply(lambda x:int(x.split('/')[1])if type(x)==str else 0 )

import matplotlib.pyplot as plt
import numpy as np

def plot_graph(x_val, y_val):
    %matplotlib inline
    plt.plot(x_val[0], y_val[0], 'bo', label='Training')
    plt.xlabel(x_val[1])
    plt.ylabel(y_val[1])
    plt.legend()
    plt.show()

plot_graph([train_df['release_year'], 'year'], [train_df['revenue'],'revenue'])

plot_graph([train_df['crew'], 'crew'], [train_df['revenue'], 'revenue'])

plot_graph([train_df['cast'], 'cast'], [train_df['revenue'], 'revenue'])

plot_graph([train_df['cast']/train_df['crew'], 'cast/crew'], [train_df['revenue'],'revenue'])

plot_graph([train_df['cast']/train_df['popularity'],'cast/popularity'], [train_df['revenue'],'revenue'])

plot_graph([train_df['cast']/train_df['genres'],'cast/genre'],[train_df['revenue'],'revenue'])

plot_graph([train_df['genres'],'genres'],[train_df['revenue'],'revenue'])

plot_graph([train_df['popularity'],'popularity'],[train_df['revenue'],'revenue'])

plot_graph([train_df['budget']/train_df['popularity'],'budget/popularity'], [train_df['revenue'], 'revenue'])

plot_graph([train_df['budget'],'budget'],[train_df['revenue'],'revenue'])

plot_graph([train_df['budget']/train_df['production_companies'], 'budget/production_companies'], [train_df['revenue'],'revenue'])

plot_graph([train_df['budget']/train_df['release_year'], 'budget/year'], [train_df['revenue'],'revenue'])

plot_graph([train_df['spoken_languages'], 'spoken_languages'], [train_df['revenue'], 'revenue'])

plot_graph([train_df['budget']/train_df['spoken_languages'], 'budget/spoken_languages'], [train_df['revenue'], 'revenue'])

plot_graph([train_df['release_year']/train_df['spoken_languages'], 'year/spoken_languages'], [train_df['revenue'], 'revenue'])

plot_graph([train_df['release_year'], 'year'], [train_df['cast'],'cast'])

plot_graph([train_df['release_year']/train_df['cast'], 'year/cast'], [train_df['revenue'], 'revenue'])


plot_graph([train_df['release_year'],'year'],[train_df['runtime'], 'runtime'])

plot_graph([train_df['release_year']/train_df['runtime'],'year/runtime'], [train_df['revenue'],'revenue'])

plot_graph([train_df['runtime'].apply(np.log),'runtime'],[train_df['revenue'].apply(np.log),'revenue'])

import seaborn as sns

df = train_df
Var_Corr = df.corr()
fig, ax = plt.subplots(figsize=(10,10))
# plot the heatmap and annotation on it
sns.heatmap(Var_Corr, xticklabels=Var_Corr.columns, yticklabels=Var_Corr.columns, annot=True,ax=ax)

yearvsrev = (df.groupby(['release_year'], as_index=False).mean())[['release_year','revenue']]

plot_graph([yearvsrev['release_year'],'year'],[yearvsrev['revenue'],'revenue'])

df_for_merge = df[['release_year']]
df_for_merge

df['avg_rev_per_year'] =pd.merge(df_for_merge, yearvsrev, how = 'left', on = "release_year")
