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


