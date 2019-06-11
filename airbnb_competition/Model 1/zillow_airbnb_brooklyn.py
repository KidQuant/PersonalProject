#%%

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

cmap = sns.diverging_palette(220, 10, as_cmap=True)

# %% Reading and cleaning the data

def read_data(location):
    location = location[['id', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'price', 'minimum_nights',
       'availability_365', 'number_of_reviews', 'review_scores_rating', 'neighbourhood', 'neighbourhood_cleansed',
       'review_scores_accuracy', 'review_scores_value']]
    return location

def get_stats(location):
    x = ['accommodates', 'bathrooms', 'bedrooms', 'price', 'minimum_nights',
       'availability_365', 'number_of_reviews', 'review_scores_rating',
       'review_scores_accuracy', 'review_scores_value']
    location = location.loc[:, x]
    location_stats = location.describe()
    location_stats = pd.concat([location_stats.ix[0:4], location_stats.ix[7:]])
    return location_stats


def reorder(location):
    new = location.set_index('location', append = True).unstack(0)
    return new

nyc = pd.read_csv('listings.csv.gz')
nyc.to_csv('listings.csv')
nyc = read_data(nyc)
nyc['price'] = nyc['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

# %% Getting Statistics on Airbnb Data

bath_beach_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Bath Beach'])
bath_beach_s['location'] = 'Bath Beach'
bath_beach_s = reorder(bath_beach_s)

bay_ridge_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Bay Ridge'])
bay_ridge_s['location'] = 'Bay Ridge'
bay_ridge_s = reorder(bay_ridge_s)

bedstuy_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Bedford-Stuyvesant'])
bedstuy_s['location'] = 'Bedford-Stuyvesant'
bedstuy_s = reorder(bedstuy_s)

bensonhurst_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Bensonhurst'])
bensonhurst_s['location'] = 'Bensonhurst'
bensonhurst_s = reorder(bensonhurst_s)

bergen_beach_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Bergen Beach'])
bergen_beach_s['location'] = 'Bergen Beach'
bergen_beach_s = reorder(bergen_beach_s)

boerum_hill_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Boerum Hill'])
boerum_hill_s['location'] = 'Boerum Hill'
boerum_hill_s = reorder(boerum_hill_s)

borough_park_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Borough Park'])
borough_park_s['location'] = 'Borough Park'
borough_park_s = reorder(borough_park_s)

brighton_beach_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Brighton Beach'])
brighton_beach_s['location'] = 'Brighton Beach'
brighton_beach_s = reorder(brighton_beach_s)

brooklyn_height_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Brooklyn Heights'])
brooklyn_height_s['location'] = 'Brooklyn Heights'
brooklyn_height_s = reorder(brooklyn_height_s)

brownsville_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Brownsville'])
brownsville_s['location'] = 'Brownsville'
brownsville_s = reorder(brownsville_s)

bushwick_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Bushwick'])
bushwick_s['location'] = 'Bushwick'
bushwick_s = reorder(bushwick_s)

canarsie_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Canarsie'])
canarsie_s['location'] = 'Canarsie'
canarsie_s = reorder(canarsie_s)

carroll_gardens_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Carroll Gardens'])
carroll_gardens_s['location'] = 'Carroll Gardens'
carroll_gardens_s = reorder(carroll_gardens_s)

clinton_hill_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Clinton Hill'])
clinton_hill_s['location'] = 'Clinton Hill'
clinton_hill_s = reorder(clinton_hill_s)

cobble_hill_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Cobble Hill'])
cobble_hill_s['location'] = 'Cobble Hill'
cobble_hill_s = reorder(cobble_hill_s)

columbia_st_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Columbia St'])
columbia_st_s['location'] = 'Columbia St'
columbia_st_s = reorder(columbia_st_s)

coney_island_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Coney Island'])
coney_island_s['location'] = 'Coney Island'
coney_island_s = reorder(coney_island_s)

crown_heights_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Crown Heights'])
crown_heights_s['location'] = 'Crown Heights'
crown_heights_s = reorder(crown_heights_s)

cypress_hills_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Cypress Hills'])
cypress_hills_s['location'] = 'Cypress Hills'
cypress_hills_s = reorder(cypress_hills_s)

downtown_brooklyn_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Downtown Brooklyn'])
downtown_brooklyn_s['location'] = 'Downtown Brooklyn'
downtown_brooklyn_s = reorder(downtown_brooklyn_s)

dumbo_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'DUMBO'])
dumbo_s['location'] = 'DUMBO'
dumbo_s = reorder(dumbo_s)

dyker_heights_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Dyker Heights'])
dyker_heights_s['location'] = 'Dyker Heights'
dyker_heights_s = reorder(dyker_heights_s)

east_flatbash_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'East Flatbush'])
east_flatbash_s['location'] = 'East Flatbush'
east_flatbash_s = reorder(east_flatbash_s)

east_ny_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'East New York'])
east_ny_s['location'] = 'East New York'
east_ny_s = reorder(east_ny_s)

flatbush_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Flatbush'])
flatbush_s['location'] = 'Flatbush'
flatbush_s = reorder(flatbush_s)

flatlands_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Flatlands'])
flatlands_s['location'] = 'Flatlands'
flatlands_s = reorder(flatlands_s)

fort_greene_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Fort Greene'])
fort_greene_s['location'] = 'Fort Greene'
fort_greene_s = reorder(fort_greene_s)

fort_hamilton_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Fort Hamilton'])
fort_hamilton_s['location'] = 'Fort Hamilton'
fort_hamilton_s = reorder(fort_hamilton_s)

gowanus_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Gowanus'])
gowanus_s['location'] = 'Gowanus'
gowanus_s = reorder(gowanus_s)

gravesend_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Gravesend'])
gravesend_s['location'] = 'Gravesend'
gravesend_s = reorder(gravesend_s)

greenpoint_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Greenpoint'])
greenpoint_s['location'] = 'Greenpoint'
greenpoint_s = reorder(greenpoint_s)

kensington_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Kensington'])
kensington_s['location'] = 'Kensington'
kensington_s = reorder(kensington_s)

manhattan_beach_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Manhattan Beach'])
manhattan_beach_s['location'] = 'Manhattan Beach'
manhattan_beach_s = reorder(manhattan_beach_s)

midwood_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Midwood'])
midwood_s['location'] = 'Midwood'
midwood_s = reorder(midwood_s)

mill_basin_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Mill Basin'])
mill_basin_s['location'] = 'Mill Basin'
mill_basin_s = reorder(mill_basin_s)

navy_yard_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Navy Yard'])
navy_yard_s['location'] = 'Navy Yard'
navy_yard_s = reorder(navy_yard_s)

park_slope_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Park Slope'])
park_slope_s['location'] = 'Park Slope'
park_slope_s = reorder(park_slope_s)

prospect_heights_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Prospect Heights'])
prospect_heights_s['location'] = 'Prospect Heights'
prospect_heights_s = reorder(prospect_heights_s)

pros_leff_gard_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Prospect-Lefferts Gardens'])
pros_leff_gard_s['location'] = 'Prospect-Lefferts Gardens'
pros_leff_gard_s = reorder(pros_leff_gard_s)

red_hook_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Red Hook'])
red_hook_s['location'] = 'Red Hook'
red_hook_s = reorder(red_hook_s)

sea_gate_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Sea Gate'])
sea_gate_s['location'] = 'Sea Gate'
sea_gate_s = reorder(sea_gate_s)

sheepshead_bay_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Sheepshead Bay'])
sheepshead_bay_s['location'] = 'Sheepshead Bay'
sheepshead_bay_s = reorder(sheepshead_bay_s)

south_slope_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'South Slope'])
south_slope_s['location'] = 'South Slope'
south_slope_s = reorder(south_slope_s)

sunset_park_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Sunset Park'])
sunset_park_s['location'] = 'Sunset Park'
sunset_park_s = reorder(sunset_park_s)

vinegar_hill_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Vinegar Hill'])
vinegar_hill_s['location'] = 'Vinegar Hill'
vinegar_hill_s = reorder(vinegar_hill_s)

williamsburg_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Williamsburg'])
williamsburg_s['location'] = 'Williamsburg'
williamsburg_s = reorder(williamsburg_s)

windsor_terrace_s = get_stats(nyc[nyc['neighbourhood_cleansed'] == 'Windsor Terrace'])
windsor_terrace_s['location'] = 'Windsor Terrace'
windsor_terrace_s = reorder(windsor_terrace_s)

statistics = pd.concat([bath_beach_s, bay_ridge_s, bedstuy_s, bensonhurst_s, bergen_beach_s, boerum_hill_s, borough_park_s,
            brighton_beach_s, brooklyn_height_s, brownsville_s, bushwick_s, canarsie_s, carroll_gardens_s, clinton_hill_s, cobble_hill_s,
            columbia_st_s, coney_island_s, crown_heights_s, cypress_hills_s, downtown_brooklyn_s, dumbo_s, dyker_heights_s, east_flatbash_s, east_ny_s,
            flatbush_s, flatlands_s, fort_greene_s, fort_hamilton_s, gowanus_s, gravesend_s, greenpoint_s, kensington_s, manhattan_beach_s,
            midwood_s, mill_basin_s, navy_yard_s, park_slope_s, prospect_heights_s, pros_leff_gard_s, red_hook_s, sea_gate_s, sheepshead_bay_s,
            south_slope_s, sunset_park_s, vinegar_hill_s, williamsburg_s, windsor_terrace_s])

statistics.index

#%%

x = {'Bath Beach': len(nyc[nyc['neighbourhood_cleansed'] == 'Bath Beach']),
      'Bay Ridge': len(nyc[nyc['neighbourhood_cleansed'] == 'Bay Ridge']),
      'Bedford-Stuyvesant':len(nyc[nyc['neighbourhood_cleansed'] == 'Bedford-Stuyvesant']),
      'Bensonhurst':len(nyc[nyc['neighbourhood_cleansed'] == 'Bensonhurst']),
      'Bergen Beach':len(nyc[nyc['neighbourhood_cleansed'] == 'Bergen Beach']),
      'Boerum Hill':len(nyc[nyc['neighbourhood_cleansed'] == 'Boerum Hill']),
      'Borough Park':len(nyc[nyc['neighbourhood_cleansed'] == 'Borough Park']),
      'Brighton Beach':len(nyc[nyc['neighbourhood_cleansed'] == 'Brighton Beach']),
      'Brooklyn Heights':len(nyc[nyc['neighbourhood_cleansed'] == 'Brooklyn Heights']),
      'Brownsville':len(nyc[nyc['neighbourhood_cleansed'] == 'Brownsville']),
      'Bushwick':len(nyc[nyc['neighbourhood_cleansed'] == 'Bushwick']),
      'Canarsie':len(nyc[nyc['neighbourhood_cleansed'] == 'Canarsie']),
      'Carroll Gardens':len(nyc[nyc['neighbourhood_cleansed'] == 'Carroll Gardens']),
      'Clinton Hill':len(nyc[nyc['neighbourhood_cleansed'] == 'Clinton Hill']),
      'Cobble Hill':len(nyc[nyc['neighbourhood_cleansed'] == 'Cobble Hill']),
      'Columbia St':len(nyc[nyc['neighbourhood_cleansed'] == 'Columbia St']),
      'Coney Island':len(nyc[nyc['neighbourhood_cleansed'] == 'Coney Island']),
      'Crown Heights':len(nyc[nyc['neighbourhood_cleansed'] == 'Crown Heights']),
      'Cypress Hills':len(nyc[nyc['neighbourhood_cleansed'] == 'Cypress Hills']),
      'Downtown Brooklyn':len(nyc[nyc['neighbourhood_cleansed'] == 'Downtown Brooklyn']),
      'DUMBO':len(nyc[nyc['neighbourhood_cleansed'] == 'DUMBO']),
      'Dyker Heights':len(nyc[nyc['neighbourhood_cleansed'] == 'Dyker Heights']),
      'East Flatbush':len(nyc[nyc['neighbourhood_cleansed'] == 'East Flatbush']),
      'East New York':len(nyc[nyc['neighbourhood_cleansed'] == 'East New York']),
      'Flatbush':len(nyc[nyc['neighbourhood_cleansed'] == 'Flatbush']),
      'Flatlands':len(nyc[nyc['neighbourhood_cleansed'] == 'Flatlands']),
      'Fort Greene':len(nyc[nyc['neighbourhood_cleansed'] == 'Fort Greene']),
      'Fort Hamilton':len(nyc[nyc['neighbourhood_cleansed'] == 'Fort Hamilton']),
      'Gowanus':len(nyc[nyc['neighbourhood_cleansed'] == 'Gowanus']),
      'Gravesend':len(nyc[nyc['neighbourhood_cleansed'] == 'Gravesend']),
      'Greenpoint':len(nyc[nyc['neighbourhood_cleansed'] == 'Greenpoint']),
      'Kensington':len(nyc[nyc['neighbourhood_cleansed'] == 'Kensington']),
      'Manhattan Beach':len(nyc[nyc['neighbourhood_cleansed'] == 'Manhattan Beach']),
      'Midwood':len(nyc[nyc['neighbourhood_cleansed'] == 'Midwood']),
      'Mill Basin':len(nyc[nyc['neighbourhood_cleansed'] == 'Mill Basin']),
      'Navy Yard':len(nyc[nyc['neighbourhood_cleansed'] == 'Navy Yard']),
      'Park Slope':len(nyc[nyc['neighbourhood_cleansed'] == 'Park Slope']),
      'Prospect Heights':len(nyc[nyc['neighbourhood_cleansed'] == 'Prospect Heights']),
      'Prospect-Lefferts Gardens':len(nyc[nyc['neighbourhood_cleansed'] == 'Prospect-Lefferts Gardens']),
      'Red Hook':len(nyc[nyc['neighbourhood_cleansed'] == 'Red Hook']),
      'Sea Gate':len(nyc[nyc['neighbourhood_cleansed'] == 'Sea Gate']),
      'Sheepshead Bay':len(nyc[nyc['neighbourhood_cleansed'] == 'Sheepshead Bay']),
      'South Slope':len(nyc[nyc['neighbourhood_cleansed'] == 'South Slope']),
      'Sunset Park':len(nyc[nyc['neighbourhood_cleansed'] == 'Sunset Park']),
      'Vinegar Hill':len(nyc[nyc['neighbourhood_cleansed'] == 'Vinegar Hill']),
      'Williamsburg':len(nyc[nyc['neighbourhood_cleansed'] == 'Williamsburg']),
      'Windsor Terrace':len(nyc[nyc['neighbourhood_cleansed'] == 'Windsor Terrace'])}

df = pd.DataFrame(x, index=[0]).stack()
df = pd.DataFrame(df).sort_values([0], ascending=[False]).reset_index(0)
df = df[0]
df = pd.DataFrame(df)
df.columns = ['Count of Listings']
df

df['Count of Listings'].plot(kind = 'bar', cmap = cmap)
plt.title('Count of Listings')


# %% Creating DataFrame of population in each metro area in millions from US Census 2015
pop = pd.read_csv('brooklyn_population.csv').convert_objects(convert_numeric=True)
pop.columns = ['City', 'Population']
pop = pop.set_index('City')

#Merging with listing data and normalizing
df1 = pd.concat([df, pop], axis= 1)
df1 = df1.astype('float')
df1['Normalized by Population'] = df1['Count of Listings'] / df1['Population']
df1.sort_values(['Normalized by Population'], ascending=[False]).reset_index(0)

z = [(365 - statistics['availability_365']['mean']).convert_objects(convert_numeric = True), df1['Normalized by Population']]
df2 = pd.concat(z, axis=1)
df2

z = [(365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True), df1['Normalized by Population']]
df2 = pd.concat(z, axis=1)

x = df2['Normalized by Population']
y = df2['mean']

n = (df2.index.tolist())

fig, ax = plt.subplots()

fig, ax = plt.subplots()
ax.scatter(x, y, c=y,cmap = cmap, s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize = 9)


#%% Average Availability of Listings
x = (365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True)
x = pd.DataFrame(x).sort_values(['mean'], ascending=[False])
x.columns = ['Availability']
x

x = pd.DataFrame(statistics['number_of_reviews']['mean'].convert_objects(convert_numeric=True)).sort_values(['mean'], ascending=[False])
x.columns = ['Avg. # of Reviews']
x

x = (365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True)
y = statistics['price']['mean'].convert_objects(convert_numeric=True)

n = (x.reset_index().location.tolist())

fig, ax = plt.subplots()
ax.scatter(x, y, c=y,cmap = cmap , s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize=10)

plt.xlabel('Average Number of Days booked in next 365 days', fontsize=14)
plt.ylabel('Average Price', fontsize=14)
plt.title('Average Price and Popularity of Listings', fontsize=14, fontweight='bold')


#%% Dropping Mill Basin

x = (365 - statistics['availability_365']['mean'].convert_objects(convert_numeric = True).drop('Mill Basin'))
y = statistics['price']['mean'].convert_objects(convert_numeric = True).drop('Mill Basin')
n = (x.reset_index()).location.tolist()

fig, ax = plt.subplots(figsize=(9, 7))
ax.scatter(x, y, c=y,cmap = cmap , s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize = 15)
    
plt.xlabel('Average Number of Days booked in next 365 days', fontsize=18)
plt.ylabel('Average Price', fontsize=18)
plt.title('Average Price and Popularity of Listings', fontsize=18, fontweight='bold')


#%% Correlation between the two variables
df = pd.concat ([x,y], axis =1 )
df.corr()

#%% Price and Average Rating Relationship

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


#%% Correlation Matrix

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


#%% The Zillow Real Estate Data

ZHVI = pd.read_csv('Zip_Zhvi_Summary_AllHomes.csv').set_index('RegionName')

x = ['Bath Beach', 'Bay Ridge', 'Bedford-Stuyvesant', 'Bensonhurst',
       'Bergen Beach', 'Boerum Hill', 'Borough Park', 'Brighton Beach',
       'Brooklyn Heights', 'Brownsville', 'Bushwick', 'Canarsie',
       'Carroll Gardens', 'Clinton Hill', 'Cobble Hill', 'Columbia St',
       'Coney Island', 'Crown Heights', 'Cypress Hills', 'Downtown Brooklyn',
       'DUMBO', 'Dyker Heights', 'East Flatbush', 'East New York', 'Flatbush',
       'Flatlands', 'Fort Greene', 'Fort Hamilton', 'Gowanus', 'Gravesend',
       'Greenpoint', 'Kensington', 'Manhattan Beach', 'Midwood', 'Mill Basin',
       'Navy Yard', 'Park Slope', 'Prospect Heights',
       'Prospect-Lefferts Gardens', 'Red Hook', 'Sea Gate', 'Sheepshead Bay',
       'South Slope', 'Sunset Park', 'Vinegar Hill', 'Williamsburg',
       'Windsor Terrace']

y = ['Zhvi', 'MoM', 'QoQ', 'YoY', '5Year', '10Year']

ZHVI = ZHVI.loc[x , y ]

df_zillow = ZHVI
df_zillow.columns = ['ZHVI', 'ZHVI_MoM', 'ZHVI_QoQ', 'ZHVI_YoY', 'ZHVI_5Year', 'ZHVI_10Year']
df_zillow

#%% Listing Trends and the Real Estate Metrics

df = pd.concat([statistics['price']['mean'], df_zillow['ZHVI']], axis = 1).dropna()

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

#%% Dropping two outliers to determine the correlation

df = df.drop(['Mill Basin', 'South Slope'])
df.corr()

df = pd.concat([statistics['price']['mean'], df_zillow['ZHVI_5Year']], axis =1).dropna()

x = df['ZHVI_5Year'] * 100
y = df['mean']

n = (df.index).tolist()

fig, ax = plt.subplots(figsize=(12, 10))
ax.scatter(x, y, c=y,cmap = cmap , s =200)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i],y[i]), fontsize = 16)
    
plt.xlabel('5 Year Home Price Growth ', fontsize=20)    
plt.ylabel('Average Price ABNB Listing', fontsize=20)
plt.title('Home Price Growth, 5 Years and ABNB Listing Price', fontsize=20, fontweight='bold')



#%% Correlation Matrix for Zillow Parameters
df2 = df_zillow
df2.columns = ['Z', 'M', 'Q', 'Y', '5', '10']
coor= df1.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(df2.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(df2.corr(), mask=mask, cmap=cmap, vmax=.3,
            square=True, xticklabels=2, yticklabels=5,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)


#%% Corrlation Matrix for Zillow parameters and Airbnb Prices

df1 = pd.DataFrame(statistics.iloc[:,17])
df = pd.concat([df1, df2], axis =1)
coor= df.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(df.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(df.corr(), mask=mask, cmap=cmap, vmax=.3,
            square=True, xticklabels=2, yticklabels=5,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

#%% Regression Model for Predicting Average Price -- Using ZHVI and Airbnb Listing Data

def read_data(location):
       location = location[['zipcode', 'accommodates', 'bathrooms', 'bedrooms', 'price', 
              'minimum_nights', 'availability_365', 'number_of_reviews', 'review_scores_rating',
              'review_scores_accuracy', 'review_scores_value']].dropna(axis =0)
       location = location.set_index('zipcode')
       return location


nyc = pd.read_csv('listings.csv.gz')
bath_beach = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Bath Beach'])
bath_beach['price'] = bath_beach['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

nyc = pd.read_csv('listings.csv.gz')
bath_beach = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Bath Beach'])
bath_beach['price'] = bath_beach['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

bay_ridge = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Bay Ridge'])
bay_ridge['price'] = bay_ridge['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

bed_stuy = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Bedford-Stuyvesant'])
bed_stuy['price'] = bed_stuy['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

bensonhurst = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Bensonhurst'])
bensonhurst['price'] = bensonhurst['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

bergen_beach = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Bergen Beach'])
bergen_beach['price'] = bergen_beach['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

boerum_hill = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Boerum Hill'])
boerum_hill['price'] = boerum_hill['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

borough_park = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Borough Park'])
borough_park['price'] = borough_park['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

brighton_beach = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Brighton Beach'])
brighton_beach['price'] = brighton_beach['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

brooklyn_heights = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Brooklyn Heights'])
brooklyn_heights['price'] = brooklyn_heights['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

brownsville = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Brownsville'])
brownsville['price'] = brownsville['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

bushwick = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Bushwick'])
bushwick['price'] = bushwick['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

canarsie = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Canarsie'])
canarsie['price'] = canarsie['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

carroll_gardens = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Carroll Gardens'])
carroll_gardens['price'] = carroll_gardens['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

clinton_hill = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Clinton Hill'])
clinton_hill['price'] = clinton_hill['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

cobble_hill = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Cobble Hill'])
cobble_hill['price'] = cobble_hill['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

columbia_st = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Columbia St'])
columbia_st['price'] = columbia_st['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

coney_island = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Coney Island'])
coney_island['price'] = coney_island['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

crown_heights = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Crown Heights'])
crown_heights['price'] = crown_heights['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

cypress_hills = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Cypress Hills'])
cypress_hills['price'] = cypress_hills['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

downtown_brooklyn = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Downtown Brooklyn'])
downtown_brooklyn['price'] = downtown_brooklyn['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

dumbo = read_data(nyc[nyc['neighbourhood_cleansed'] == 'DUMBO'])
dumbo['price'] = dumbo['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

dyker_heights = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Dyker Heights'])
dyker_heights['price'] = dyker_heights['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

east_flatbush = read_data(nyc[nyc['neighbourhood_cleansed'] == 'East Flatbush'])
east_flatbush['price'] = east_flatbush['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

east_newyork = read_data(nyc[nyc['neighbourhood_cleansed'] == 'East New York'])
east_newyork['price'] = east_newyork['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

flatbush = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Flatbush'])
flatbush['price'] = flatbush['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

flatlands = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Flatlands'])
flatlands['price'] = flatlands['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

fort_greene = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Fort Greene'])
fort_greene['price'] = fort_greene['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

fort_hamilton = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Fort Hamilton'])
fort_hamilton['price'] = fort_hamilton['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

gowanus = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Gowanus'])
gowanus['price'] = gowanus['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

gravesend = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Gravesend'])
gravesend['price'] = gravesend['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

greenpoint = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Greenpoint'])
greenpoint['price'] = greenpoint['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

kensington = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Kensington'])
kensington['price'] = kensington['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

manhattan_beach = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Manhattan Beach'])
manhattan_beach['price'] = manhattan_beach['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

midwood = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Midwood'])
midwood['price'] = midwood['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

mill_basin = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Mill Basin'])
mill_basin['price'] = mill_basin['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

navy_yard = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Navy Yard'])
navy_yard['price'] = navy_yard['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

park_slope = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Park Slope'])
park_slope['price'] = park_slope['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

prospect_heights = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Prospect Heights'])
prospect_heights['price'] = prospect_heights['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

pros_leff = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Prospect-Lefferts Gardens'])
pros_leff['price'] = pros_leff['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

red_hook = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Red Hook'])
red_hook['price'] = red_hook['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

sea_gate = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Sea Gate'])
sea_gate['price'] = sea_gate['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

sheepshead_bay = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Sheepshead Bay'])
sheepshead_bay['price'] = sheepshead_bay['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

south_slope = read_data(nyc[nyc['neighbourhood_cleansed'] == 'South Slope'])
south_slope['price'] = south_slope['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

sunset_park = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Sunset Park'])
sunset_park['price'] = sunset_park['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

vinegar_hill = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Vinegar Hill'])
vinegar_hill['price'] = vinegar_hill['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

williamsburg = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Williamsburg'])
williamsburg['price'] = williamsburg['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

windsor_terrace = read_data(nyc[nyc['neighbourhood_cleansed'] == 'Windsor Terrace'])
windsor_terrace['price'] = windsor_terrace['price'].map(lambda x: str(x)[1:]).convert_objects(convert_numeric=True)

#DataFrame with all listings and Airbnb features:
df_abnb = pd.concat([bath_beach, bay_ridge, bed_stuy, bensonhurst, bergen_beach, boerum_hill, borough_park, brighton_beach,
              brooklyn_heights, brownsville, bushwick, canarsie, carroll_gardens, clinton_hill, cobble_hill, columbia_st,
              coney_island, crown_heights, cypress_hills, downtown_brooklyn, dumbo, dyker_heights, east_flatbush, east_newyork,
              flatbush, flatlands, fort_greene, fort_hamilton, gowanus, gravesend, greenpoint, kensington, manhattan_beach, 
              midwood, mill_basin, park_slope, prospect_heights, pros_leff, red_hook, sunset_park, vinegar_hill, williamsburg,
              windsor_terrace])

df_abnb

#DataFrame with Zillow Feature: Zillow Home Value Index
ZHVI = pd.read_csv('Zip_Zhvi_Summary_AllHomes.csv').set_index('RegionName')
ZHVI = ZHVI.ix[:,[7,11,12]]

# Merge on Zipcode
df1 = pd.merge(df_abnb, ZHVI, left_index = True, right_index = True).dropna()
df1['reviewtotal'] = (df1['review_scores_rating'] + df1['review_scores_accuracy'] + df1['review_scores_value'])


#%% Linearity of Features with Dependent Variable: Price / Availability and Pice / # of Reviews

x = np.log(df1['availability_365'])
y = df1['price']

fig, ax = plt.subplots()
ax.scatter(x,y, c ='c', alpha = .5)
plt.ylim(0,1000)
plt.xlim(-0.01, 1.75)

plt.xlabel('Log of Availability', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.title('Price and Availability', fontsize=14, fontweight='bold')

x1 = np.log(df1['number_of_reviews'])
y1 = df1['price']

fig, ax = plt.subplots()
ax.scatter(x1, y1, c='r', alpha=.5)
plt.ylim(0,1000)
plt.xlim(-0.01, 1.75)

plt.xlabel('Log of # of Reviews', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.title('Price and # of Reviews', fontsize=14, fontweight='bold')


#%% #%% Linearity of Features with Dependent Variable: Price / Median Home Values

x2 = (df1['Zhvi'])
y2 = df1['price']

fig, ax = plt.subplots()
ax.scatter(x2, y2, c = 'r', alpha = 0.5)
plt.ylim(0,1000)
plt.xlim(200000,1400000)

plt.xlabel('ZHVI (Median Home Price)', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.title('Price and Median Home Value (ZHVI)', fontsize=14, fontweight='bold')

x = (df1['10Year'])
y = df1['price']

fig, ax = plt.subplots()
ax.scatter(x, y, c ='c', alpha = 0.5)
plt.ylim(0,1000)
plt.xlim(-0.02, 0.06)

plt.xlabel('10 Year Change in ZHVI (Median Home price)', fontsize=14)
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

#%% The Model

#The merged features dataframe
df1 = pd.merge(df_abnb, ZHVI, left_index = True, right_index = True).dropna()
df1['reviewtotal'] = (df1['review_scores_rating'] + df1['review_scores_accuracy'] + df1['review_scores_value'])

#Trainsforming:
df1['number_of_reviews'] = np.log(df1['number_of_reviews'])
df1['availability_365'] = np.log(df1['availability_365'])

#Final Features dataframe
features = df1[['Zhvi', 'number_of_reviews', 'availability_365', 'reviewtotal', '10Year', '5Year',
              'accommodates', 'bathrooms']].replace([np.inf, -np.inf], np.nan).fillna(0)

features.corr()

#%% Model Evaluation

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = features
Y = pd.DataFrame(df1['price']).fillna(0)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, Y_train)

print('R-squared on Training Data:', r2_score(Y_train, clf.predict(X_train)))
print('R-squared on Testing Data:', r2_score(Y_test, clf.predict(X_test)))

from sklearn.metrics import mean_squared_error

print('R-squared on Test set:', mean_squared_error(Y_test, clf.predict(X_test)))
print('R-squared on Testing Data:', mean_squared_error(Y_train, clf.predict(X_train)))

coef_df = pd.concat([pd.DataFrame(features.columns), pd.DataFrame(clf.coef_).transpose()], axis=1)
coef_df.columns = ['Feature', 'Regression Coefficient']
coef_df

import matplotlib.patches as mpatches

plt.figure(figsize=(10,6))
plt.scatter(clf.predict(X_train), clf.predict(X_train) - Y_train, c='c', s=40, alpha=0.5)
plt.scatter(clf.predict(X_test), clf.predict(X_test) - Y_test, c='r', s=40, alpha=0.65)
plt.hlines(y = 0, xmin=-30, xmax= 50)
plt.title('Residuals vs Fitted Values')
plt.ylabel('Residuals')
plt.xlabel('Fitted Values')


#%% Using the Random Forest Regression Model

from sklearn.ensemble import RandomForestRegressor

X = features
Y = pd.DataFrame(df1['price']).fillna(0)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

rf = RandomForestRegressor(random_state=1)
rf.fit(X_train, Y_train)

print('R-squared for training data: ', rf.score(X_train, Y_train))
print('R-squared for test data: ',rf.score(X_test, Y_test))

from sklearn.metrics import mean_squared_error
print('Mean squared error on the test set: ', mean_squared_error(Y_test, rf.predict(X_test)))
print('Mean squared error on the training set: ', mean_squared_error(Y_train, rf.predict(X_train)))

plt.scatter(rf.predict(X_test), Y_test.as_matrix())
plt.title('Random Forest: Predicted vs. Actual Price')
plt.xlabel('Predict Listing Price')
plt.ylabel('Actual Listing Price')
plt.xlim(0,1000)

x = df1.price
sns.distplot(x, kde=False)
plt.title('Distribution of Price')


