
#%% 

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import *
%matplotlib inline 

import warnings
warnings.filterwarnings('ignore')

cmap = sns.diverging_palette(220, 10, as_cmap=True)

#%%

def read_data(location):
    location = location[['id', 'neighbourhood_group_cleansed','room_type', 'accommodates', 'bathrooms', 'bedrooms', 'price', 'minimum_nights',
       'availability_365', 'number_of_reviews', 'review_scores_rating',
       'review_scores_accuracy', 'review_scores_value']]
    return location

def get_stats(location):
    x = ['neighbourhood_group_cleansed','accommodates', 'bathrooms', 'bedrooms', 'price', 'minimum_nights',
       'availability_365', 'number_of_reviews', 'review_scores_rating',
       'review_scores_accuracy', 'review_scores_value']
    location = location.loc[:, x]
    location_stats = location.describe()
    location_stats = concat([location_stats.ix[0:4], location_stats.ix[7:]])
    return location_stats

def reorder(location):
    new = location.set_index('location', append = True).unstack(0)
    return new


#%%

new_york = read_csv('DataScience\listings.csv.gz')
new_york = read_data(new_york)
new_york['price'] = new_york['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

new_york.head()

#%%

#Brooklyn
brooklyn = new_york[(new_york['neighbourhood_group_cleansed'] == 'Brooklyn')]
brooklyn.head()
brooklyn.reset_index(inplace=True)
brooklyn =  brooklyn.drop('index', axis =1)

#Bronx
bronx = new_york[(new_york['neighbourhood_group_cleansed'] == 'Bronx')]
bronx.head()
bronx.reset_index(inplace=True)
bronx =  bronx.drop('index', axis =1)

#Manhattan 
manhattan = new_york[(new_york['neighbourhood_group_cleansed'] == 'Manhattan')]
manhattan.head()
manhattan.reset_index(inplace=True)
manhattan =  manhattan.drop('index', axis =1)

#Queens
queens = new_york[(new_york['neighbourhood_group_cleansed'] == 'Queens')]
queens.head()
queens.reset_index(inplace=True)
queens =  queens.drop('index', axis =1)

#Staten Island
staten_island = new_york[(new_york['neighbourhood_group_cleansed'] == 'Staten Island')]
staten_island.head()
staten_island.reset_index(inplace=True)
queens =  staten_island.drop('index', axis =1)

#%%

brooklyn_s = get_stats(brooklyn)
brooklyn_s['location'] = 'Brooklyn, NY'
brooklyn_s = reorder(brooklyn_s)

bronx_s = get_stats(brooklyn)
bronx_s['location'] = 'Bronx, NY'
bronx_s = reorder(bronx_s)

manhattan_s = get_stats(brooklyn)
manhattan_s['location'] = 'Manhattan, NY'
manhattan_s = reorder(manhattan_s)
manhattan.head()


queens_s = get_stats(brooklyn)
queens_s['location'] = 'Queens, NY'
queens_s = reorder(queens_s)

staten_island_s = get_stats(brooklyn)
staten_island_s['location'] = 'Staten Island, NY'
staten_island_s = reorder(staten_island_s)

#%%

statistics = concat([brooklyn_s, bronx_s, manhattan_s, queens_s, staten_island_s])
statistics

statistics.columns.values

#%%

x = {'Brooklyn, NY': len(brooklyn), 'Bronx, NY' : len(bronx), 
     'Manhattan, NY' : len(manhattan), 'Queens, NY' : len(queens), 
     'Staten Island, NY': len(staten_island) }

df = DataFrame(x, index=[0]).stack()
df = DataFrame(df).sort_values([0], ascending=[False]).reset_index(0)
df = df[0]
df = DataFrame(df)
df.columns = ['Count of Listings']
df

df['Count of Listings'].plot(kind = 'bar', cmap = cmap)
plt.title('Count of Listings')


#Normalizing for Population
#%%

pop = read_csv('pop_cities_census.csv').convert_objects(convert_numeric=True)
pop.columns = ['City', 'Population']
pop = pop.set_index('City')

