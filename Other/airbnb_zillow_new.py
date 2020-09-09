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

#%%

austin = read_csv('DataScience\_austin.csv')
austin = read_data(austin)
austin['price'] = austin['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

boston = read_csv('DataScience\_boston.csv')
boston = read_data(boston)
boston['price'] = boston['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

dc = read_csv('DataScience\_dc.csv.gz')
dc = read_data(dc)
dc['price'] = dc['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

denver = read_csv('DataScience\_denver.csv.gz')
denver = read_data(denver)
denver['price'] = denver['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

la = read_csv('DataScience\la.csv.gz')
la = read_data(la)
la['price'] = la['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

nashville = read_csv('DataScience\_nashville.csv')
nashville = read_data(nashville)
nashville['price'] = nashville['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

nyc = read_csv('DataScience\_nyc.csv.gz')
nyc = read_data(nyc)
nyc['price'] = nyc['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

portland = read_csv('DataScience\portland.csv')
portland = read_data(portland)
portland['price'] = portland['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

sandiego = read_csv('DataScience\sandiego.csv')
sandiego = read_data(sandiego)
sandiego['price'] = sandiego['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

seattle = read_csv('DataScience\seattle.csv')
seattle = read_data(seattle)
seattle['price'] = seattle['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

sf = read_csv('DataScience\sf.csv.gz')
sf = read_data(sf)
sf['price'] = sf['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

neworleans = read_csv('DataScience\_new_orleans.csv')
neworleans = read_data(neworleans)
neworleans['price'] = neworleans['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

#%%

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

#%%

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
pop = read_csv('DataScience\pop_cities_census_usa.csv').convert_objects(convert_numeric=True)
pop.columns = ['City', 'Population']
pop = pop.set_index('City')

#Merging with listing data and normalizing
df1 = concat([df, pop], axis= 1)
df1 = df1.astype('float')
df1['Normalized by Population'] = df1['Count of Listings'] / df1['Population']
df1.sort_values(['Normalized by Population'], ascending=[False]).reset_index(0)
df

#%%
#Estimating 'Supply' and 'Demand' of Listings: Popularity and Normalized Count of Listings

z = [(365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True), df1['Normalized by Population']]
df2 = concat(z, axis = 1)
df2

x = df2['Normalized by Population']
y = df2['mean']

n = (df2.index.tolist())

fig, ax = plt.subplots()
ax.scatter(x, y, c=y,cmap = cmap, s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize = 9)
    
    
plt.xlabel('Listing Count (Normalized)', fontsize=14)
plt.ylabel('Booked Days in the next Calendar Year', fontsize=14)
plt.title('Popularity and Normalized Listing Count', fontsize=14, fontweight='bold')


#%%
#Price and Normalized Listing Count

z = [statistics['price']['mean'].convert_objects(convert_numeric=True), df1['Normalized by Population']]
df2 = concat(z, axis = 1)

x = df2['Normalized by Population']
y = df2['mean']

n = (df2.index.tolist())

fig, ax = plt.subplots()
ax.scatter(x, y, c=y,cmap = cmap, s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize = 10)
    
    
plt.xlabel('Listing Count (Normalized)', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.title('Price and Normalized Listing Count', fontsize=14, fontweight='bold')

df2.corr()

#%%
#Average Availability of Listings: What cities are more popular to visit?

x = (365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True)
x = DataFrame(x).sort_values(['mean'], ascending=[False])
x.columns = ['Availability']
x

x = DataFrame(statistics['number_of_reviews']['mean'].convert_objects(convert_numeric=True)).sort_values(['mean'], ascending=[False])
x.columns = ['Avg. # of Reviews']
x

#%%
#Price and Availibility Listings: What the relationship between the popularity of a listing and its price?

x = (365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True)
y = statistics['price']['mean'].convert_objects(convert_numeric=True)

n = (x.reset_index()).location.tolist()

fig, ax = plt.subplots()
ax.scatter(x, y, c=y,cmap = cmap , s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize = 10)
    
    
plt.xlabel('Average Number of Days booked in next 365 days', fontsize=14)
plt.ylabel('Average Price', fontsize=14)
plt.title('Average Price and Popularity of Listings', fontsize=14, fontweight='bold')

#%%
#Price and Average Rating: How does the average quality of a listing coorelate to the average price?

x = statistics['review_scores_rating']['mean'].convert_objects(convert_numeric=True)
y = statistics['price']['mean'].convert_objects(convert_numeric=True)

n = (x.reset_index()).location.tolist()

fig, ax = plt.subplots()
ax.scatter(x, y, c=y,cmap = cmap, s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize = 10)
    
    
plt.xlabel('Average Rating', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.title('Price and Average Rating', fontsize=14, fontweight='bold')


#%%
#Coorelation Matrix for Airbnb Listing Data: Which Airbnb metrics are related to each other and how?

df1 = statistics.iloc[:,[2,7,12,17,22,27,32,37,42,47]].reset_index().drop('location',axis = 1).fillna(0)
df1.columns = df1.columns.droplevel(1)
df1.columns = ['acc', 'bt', 'bd', 'pr', 'min', '365', '#rev', 'rat', "acc", "val"]
#df_zillow = df_zillow['ZHVI_10Year']
#df1 = concat([df1, df_zillow], axis = 1).fillna(0)

coor= df1.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(df1.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(df1.corr(), mask=mask, cmap=cmap, vmax=.3,
            square=True, xticklabels=2, yticklabels=5,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)


#%%
#Zillow Home Value Index (Median Home Value):

ZHVI = read_csv('DataScience\Metro_Zhvi_Summary_AllHomes.csv', encoding = 'latin1').set_index('RegionName')


x = ['Austin, TX', 'Boston, MA', 'Washington, DC', 'Denver, CO', 'Los Angeles-Long Beach-Anaheim, CA', 'Nashville, TN', 'New York, NY', 'Portland, OR', 'San Diego, CA', 'Seattle, WA', 'San Francisco, CA', 'New Orleans, LA']
y = ['Zhvi', 'MoM', 'QoQ', 'YoY', '5Year', '10Year']

ZHVI = ZHVI.loc[x , y ]

df_zillow = ZHVI
df_zillow.columns = ['ZHVI', 'ZHVI_MoM', 'ZHVI_QoQ', 'ZHVI_YoY', 'ZHVI_5Year', 'ZHVI_10Year']
df_zillow

#%%

#How does the median home price of a city influence the price of an Airbnb listing?

df = concat([statistics['price']['mean'], df_zillow['ZHVI']], axis = 1).dropna()

x = df['ZHVI']
y = df['mean']


n = (df.index).tolist()

fig, ax = plt.subplots(figsize=(12, 10))
ax.scatter(x, y, c=y,cmap = cmap, s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize = 16)
    
    
plt.xlabel('Median Home Price', fontsize=20)
plt.ylabel('Average Price ABNB Listing', fontsize=20)
plt.title('Home Price(ZHVI) and Airbnb Listing Price', fontsize=20, fontweight='bold')

df.corr()

#%%
#How does the change in home price over five years coorelate to the price? Are listings in emerging cities, with high growth, priced at a higher value?

df = concat([statistics['price']['mean'], df_zillow['ZHVI_5Year']], axis = 1).dropna()

x = df['ZHVI_5Year'] *100
y = df['mean']

n = (df.index).tolist()

fig, ax = plt.subplots(figsize=(12, 10))
ax.scatter(x, y, c=y,cmap = cmap , s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize = 16)
    
plt.xlabel('5 Year Home Price Growth ', fontsize=20)    
plt.ylabel('Average Price ABNB Listing', fontsize=20)
plt.title('Home Price Growth, 5 Years and ABNB Listing Price', fontsize=20, fontweight='bold')

#%%
# Regression Model for Predicting Average Price -- Using the ZHVI and Airbnb Listing Data

def read_data(location):
    location = location[['zipcode', 'accommodates', 'bathrooms', 'bedrooms', 'price', 'minimum_nights',
       'availability_365', 'number_of_reviews', 'review_scores_rating',
       'review_scores_accuracy', 'review_scores_value']].dropna(axis = 0)
    location = location.set_index('zipcode')
    return location

# We are going to join the Zillow data and Airbnb data according to the zip code of the listing 
# to achieve more granularilty when looking at the real estate data for each listing.

austin = read_csv('DataScience\_austin.csv')
austin = read_data(austin)
austin['price'] = austin['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

boston = read_csv('DataScience\_boston.csv')
boston = read_data(boston)
boston['price'] = boston['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

dc = read_csv('DataScience\_dc.csv.gz')
dc = read_data(dc)
dc['price'] = dc['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

denver = read_csv('DataScience\_denver.csv.gz')
denver = read_data(denver)
denver['price'] = denver['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

la = read_csv('DataScience\la.csv.gz')
la = read_data(la)
la['price'] = la['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

nashville = read_csv('DataScience\_nashville.csv')
nashville = read_data(nashville)
nashville['price'] = nashville['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

nyc = read_csv('DataScience\_nyc.csv.gz')
nyc = read_data(nyc)
nyc['price'] = nyc['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

portland = read_csv('DataScience\portland.csv')
portland = read_data(portland)
portland['price'] = portland['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

sandiego = read_csv('DataScience\sandiego.csv')
sandiego = read_data(sandiego)
sandiego['price'] = sandiego['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

seattle = read_csv('DataScience\seattle.csv')
seattle = read_data(seattle)
seattle['price'] = seattle['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

sf = read_csv('DataScience\sf.csv.gz')
sf = read_data(sf)
sf['price'] = sf['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

neworleans = read_csv('DataScience\_new_orleans.csv')
neworleans = read_data(neworleans)
neworleans['price'] = neworleans['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

#DataFrame with all listings and Airbnb features:
df_abnb = concat([austin, boston, dc, denver, la, nashville, nyc, portland, sandiego, seattle, sf, neworleans])

#DataFrame with Zillow Feature: Zillow Home Value Index
ZHVI = read_csv('DataScience\Zip_Zhvi_Summary_AllHomes.csv', encoding = 'latin1').set_index('RegionName')
ZHVI = ZHVI.ix[:,[7,11,12]]
ZHVI

# Merge on Zipcode
df1 = merge(df_abnb, ZHVI, left_index = True, right_index = True).dropna()


df1['reviewtotal'] = (df1['review_scores_rating'] + df1['review_scores_accuracy'] + df1['review_scores_value'])

df1.head()

# %%
#  Price and Features: Linearity of Features with Dependent Variable, Price

x = np.log(df1['availability_365'])
y = df1['price']

fig, ax = plt.subplots()
ax.scatter(x, y, c= 'c', alpha = .5)
plt.ylim(0,1000)
plt.xlim(-.01,1.75)

plt.xlabel('Log of Availability', fontsize=14)   
plt.ylabel('Price', fontsize=14)
plt.title('Price and Availability', fontsize=14, fontweight='bold')

x1 = np.log(df1['number_of_reviews'])
y1 = df1['price']

fig, ax = plt.subplots()
ax.scatter(x1, y1, c= 'r', alpha = .5)
plt.ylim(0,1000)
plt.xlim(-.01,1.75)

plt.xlabel('Log of # of Reviews', fontsize=14)   
plt.ylabel('Price', fontsize=14)
plt.title('Price and # of Reviews', fontsize=14, fontweight='bold')

#Price and ZHVI (Median Home Value) & Price and 5, 10 Year change in ZHVI

x2 = (df1['Zhvi'])
y2 = df1['price']

fig, ax = plt.subplots()
ax.scatter(x2, y2, c= 'r', alpha = .5)
plt.ylim (0,1000)
plt.xlim (200000,1400000)

plt.xlabel('ZHVI (Median Home Price)', fontsize=14)   
plt.ylabel('Price', fontsize=14)
plt.title('Price and Median Home Value (ZHVI)', fontsize=14, fontweight='bold')


x = (df1['10Year'])
y = df1['price']

fig, ax = plt.subplots()
ax.scatter(x, y, c= 'c', alpha = .5)
plt.ylim (0,1000)
plt.xlim(-.02,.06)

plt.xlabel('10 Year Change in  ZHVI (Median Home Price)', fontsize=14)   
plt.ylabel('Price', fontsize=14)
plt.title('Price and 10 Year Median Home Value (ZHVI)', fontsize=14, fontweight='bold')


x1 = (df1['5Year'])
y1 = df1['price']

fig, ax = plt.subplots()
ax.scatter(x1, y1, c= 'm', alpha = .5)

plt.xlabel('5 Year Change in ZHVI (Median Home Price)', fontsize=14)   
plt.ylabel('Price', fontsize=14)
plt.title('Price and 5 Year Median Home Value (ZHVI)', fontsize=14, fontweight='bold')
plt.ylim (0,1000)
plt.xlim(.045,.15)

x = (df1['reviewtotal'])
y = df1['price']

fig, ax = plt.subplots()
ax.scatter(x, y, c= 'c', alpha = .5)
plt.ylim (0,1000)
plt.xlim(20 ,122)

plt.xlabel('Sum of Ratings', fontsize=14)   
plt.ylabel('Price', fontsize=14)
plt.title('Sum of Ratings', fontsize=14, fontweight='bold')

x1 = np.log(df1['bedrooms'])
y1 = df1['price']

fig, ax = plt.subplots()
ax.scatter(x1, y1, c = 'r', alpha = .5)
plt.ylim (0,1000)
plt.xlim(-.1 ,2)

plt.xlabel('# of Bedrooms', fontsize=14)   
plt.ylabel('Price', fontsize=14)
plt.title('# of Bedrooms and Price', fontsize=14, fontweight='bold')

x1 = df1['bedrooms']
x2 = df1['bathrooms']
x3 = df1['accommodates']

y1 = df1['price']


fig, ax = plt.subplots()
ax.scatter(x1, y1, c= 'c', alpha = .5)
ax.scatter(x2, y1, c='r', alpha = .5)
ax.scatter(x3, y1, c='m', alpha = .5)
plt.ylim (-2,1000)
plt.xlim(-.1 ,17)

plt.xlabel('# of Bedrooms, Bathrooms, Accommodates', fontsize=14)   
plt.ylabel('Price', fontsize=14)
plt.title('# of Bedrooms/Bathroom/Accommodates and Price', fontsize=14, fontweight='bold')

#%%
#Linear Model using all cities and all features

df1 = merge(df_abnb, ZHVI, left_index = True, right_index = True).dropna()
df1['reviewtotal'] = (df1['review_scores_rating'] + df1['review_scores_accuracy'] + df1['review_scores_value'])

#Transforming:
df1['number_of_reviews'] = np.log(df1['number_of_reviews'])
df1['availability_365'] = np.log(df1['availability_365'])

#Final Features dataframe
features = df1[[ 'Zhvi', ]].replace([np.inf, -np.inf], np.nan).fillna(0)
features2 = df1[[ 'Zhvi', 'number_of_reviews', ]].replace([np.inf, -np.inf], np.nan).fillna(0)
features3 = df1[[ 'Zhvi', 'number_of_reviews', 'availability_365',]].replace([np.inf, -np.inf], np.nan).fillna(0)
features4 = df1[[ 'Zhvi', 'number_of_reviews', 'availability_365', 'reviewtotal', ]].replace([np.inf, -np.inf], np.nan).fillna(0)
features5 = df1[[ 'Zhvi', 'number_of_reviews', 'availability_365', 'reviewtotal', '10Year', ]].replace([np.inf, -np.inf], np.nan).fillna(0)
features6 = df1[[ 'Zhvi', 'number_of_reviews', 'availability_365', 'reviewtotal', '10Year', '5Year', ]].replace([np.inf, -np.inf], np.nan).fillna(0)
features7 = df1[[ 'Zhvi', 'number_of_reviews', 'availability_365', 'reviewtotal', '10Year', '5Year', 'accommodates']].replace([np.inf, -np.inf], np.nan).fillna(0)
features8 = df1[[ 'Zhvi', 'number_of_reviews', 'availability_365', 'reviewtotal', '10Year', '5Year', 'accommodates', 'bathrooms']].replace([np.inf, -np.inf], np.nan).fillna(0)


#%%
#Model Evaluation:

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error

X = features
X2 = features2
X3 = features3
X4 = features4
X5 = features5
X6 = features6
X7 = features7
X8 = features8
X9 = features9

y = DataFrame(df1['price']).fillna(0)
X = sm.add_constant(X)

model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

#model 2

X2 = sm.add_constant(X2)

model2 = sm.OLS(y, X2)
results2 = model2.fit()
print(results2.summary())

#model 3

X3 = sm.add_constant(X3)

model3 = sm.OLS(y, X3)
results3 = model3.fit()
print(results3.summary())

#model 4

X4 = sm.add_constant(X4)

model4 = sm.OLS(y, X4)
results4 = model4.fit()
print(results4.summary())

#model 5

X5 = sm.add_constant(X5)

model5 = sm.OLS(y, X5)
results5 = model5.fit()
print(results5.summary())

#model 6

X6 = sm.add_constant(X6)

model6 = sm.OLS(y, X6)
results6 = model6.fit()
print(results6.summary())

#model 7

X7 = sm.add_constant(X7)

model7 = sm.OLS(y, X7)
results7 = model7.fit()
print(results7.summary())

#model 8

X8 = sm.add_constant(X8)

model8 = sm.OLS(y, X8)
results8 = model8.fit()
print(results8.summary())