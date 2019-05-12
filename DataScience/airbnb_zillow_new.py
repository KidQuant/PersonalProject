import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import *
%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

cmap = sns.diverging_palette(220, 10, as_cmap=True)

def read_data(location):
    location = location[['id', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'price', 'minimum_nights',
       'availability_365', 'number_of_reviews', 'review_scores_rating',
       'review_scores_accuracy', 'review_scores_value']]
    return location

def get_stats(location):
    x = ['accommodates', 'bathrooms', 'bedrooms', 'price', 'minimum_nights',
       'availability_365', 'number_of_reviews', 'review_scores_rating',
       'review_scores_accuracy', 'review_scores_value']
    location = location.loc[:, x]
    location_stats = location.describe()
    location_stats = concat([location_stats.ix[0:4], location_stats.ix[7:]])
    return location_stats

def reorder(location):
    new = location.set_index('location', append = True).unstack(0)
    return new

austin = read_csv('austin.csv')
austin = read_data(austin)
austin['price'] = austin['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

boston = read_csv('boston.csv')
boston = read_data(boston)
boston['price'] = boston['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

dc = read_csv('dc.csv')
dc = read_data(dc)
dc['price'] = dc['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

denver = read_csv('denver.csv')
denver = read_data(denver)
denver['price'] = denver['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

la = read_csv('la.csv')
la = read_data(la)
la['price'] = la['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

nashville = read_csv('nashville.csv')
nashville = read_data(nashville)
nashville['price'] = nashville['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

nyc = read_csv('nyc.csv')
nyc = read_data(nyc)
nyc['price'] = nyc['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

portland = read_csv('portland.csv')
portland = read_data(portland)
portland['price'] = portland['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

sandiego = read_csv('sandiego.csv')
sandiego = read_data(sandiego)
sandiego['price'] = sandiego['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

seattle = read_csv('seattle.csv')
seattle = read_data(seattle)
seattle['price'] = seattle['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

sf = read_csv('sf.csv')
sf = read_data(sf)
sf['price'] = sf['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

neworleans = read_csv('new_orleans.csv')
neworleans = read_data(neworleans)
neworleans['price'] = neworleans['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)


# Getting the statistics

austin_s = get_stats(austin)
austin_s['location'] = 'Austin, TX'
austin_s = reorder(austin_s)

boston_s = get_stats(boston)
boston_s['location'] = 'Boston, MA'
boston_s = reorder(boston_s)

dc_s = get_stats(dc)
dc_s['location'] = 'Washington, DC'
dc_s = reorder(dc_s)

denver_s = get_stats(denver)
denver_s['location'] = 'Denver, CO'
denver_s = reorder(denver_s)

la_s = get_stats(la)
la_s['location'] = 'Los Angeles-Long Beach-Anaheim, CA'
la_s = reorder(la_s)

nashville_s = get_stats(nashville)
nashville_s['location'] = 'Nashville, TN'
nashville_s = reorder(nashville_s)

nyc_s = get_stats(nyc)
nyc_s['location'] = 'New York, NY'
nyc_s = reorder(nyc_s)

portland_s = get_stats(portland)
portland_s['location'] = 'Portland, OR'
portland_s = reorder(portland_s)

sandiego_s = get_stats(sandiego)
sandiego_s['location'] = 'San Diego, CA'
sandiego_s = reorder(sandiego_s)

seattle_s = get_stats(seattle)
seattle_s['location'] = 'Seattle, WA'
seattle_s = reorder(seattle_s)

sf_s = get_stats(sf)
sf_s['location'] = 'San Francisco, CA'
sf_s = reorder(sf_s)

neworleans_s = get_stats(neworleans)
neworleans_s['location'] = 'New Orleans, LA'
neworleans_s = reorder(neworleans_s)

statistics = concat([austin_s, boston_s, dc_s, denver_s, la_s, nashville_s, nyc_s, portland_s, sandiego_s, seattle_s, sf_s, neworleans_s])
statistics

statistics.columns.values

x = {'Austin, TX': len(austin), 'Boston, MA' : len(boston),
     'Washington, DC' : len(dc), 'Denver, CO' : len(denver),
     'Los Angeles-Long Beach-Anaheim, CA': len(la), 'Nashville, TN': len(nashville),
     'New York, NY': len(nyc), 'Portland, OR' : len(portland),
     'San Diego, CA' : len(sandiego), 'Seattle, WA' : len(seattle),
     'San Francisco, CA' : len(sf), 'New Orleans, LA' : len(neworleans) }

df = DataFrame(x, index=[0]).stack()
df = DataFrame(df).sort_values([0], ascending=[False]).reset_index(0)
df = df[0]
df = DataFrame(df)
df.columns = ['Count of Listings']
df

df['Count of Listings'].plot(kind = 'bar', cmap = cmap)
plt.title('Count of Listings')

# Creating DataFrame of population in each metro area in millions from US Census 2015
pop = read_csv('pop_cities_census.csv').convert_objects(convert_numeric=True)
pop.columns = ['City', 'Population']
pop = pop.set_index('City')

#Merging with listing data and normalizing
df1 = concat([df, pop], axis= 1)
df1 = df1.astype('float')
df1['Normalized by Population'] = df1['Count of Listings'] / df1['Population']
df1.sort_values(['Normalized by Population'], ascending=[False]).reset_index(0)

B
