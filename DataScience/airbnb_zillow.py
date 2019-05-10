
#%% 

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import *

%matplotlib inline 

import warnings
warnings.filterwarnings('ignore')

cmap = sns.diverging_palette(220, 10, as_cmap=True)

#%%

def read_data(location):
    location = location[['id', 'neighbourhood_cleansed','room_type', 'accommodates', 'bathrooms', 'bedrooms', 'price', 'minimum_nights',
       'availability_365', 'number_of_reviews', 'review_scores_rating',
       'review_scores_accuracy', 'review_scores_value']]
    return location

def get_stats(location):
    x = ['neighbourhood_cleansed','accommodates', 'bathrooms', 'bedrooms', 'price', 'minimum_nights',
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

new_york.to_csv('DataScience/airbnb_data.csv')

#%%

#Brooklyn
east_flatbush = new_york[(new_york['neighbourhood_cleansed'] == 'East Flatbush')]
east_flatbush.head()
east_flatbush.reset_index(inplace=True)
east_flatbush =  east_flatbush.drop('index', axis =1)

bensonhurst = new_york[(new_york['neighbourhood_cleansed'] == 'Bensonhurst')]
bensonhurst.head()
bensonhurst.reset_index(inplace=True)
bensonhurst =  bensonhurst.drop('index', axis =1)

navy_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Navy Hill')]
navy_hill.head()
navy_hill.reset_index(inplace=True)
navy_hill =  navy_hill.drop('index', axis =1)

williamsburg = new_york[(new_york['neighbourhood_cleansed'] == 'Williamsburg')]
williamsburg.head()
williamsburg.reset_index(inplace=True)
williamsburg =  williamsburg.drop('index', axis =1)

city_island = new_york[(new_york['neighbourhood_cleansed'] == 'City Island')]
city_island.head()
city_island.reset_index(inplace=True)
city_island =  city_island.drop('index', axis =1)

bay_ridge = new_york[(new_york['neighbourhood_cleansed'] == 'Bay Ridge')]
bay_ridge.head()
bay_ridge.reset_index(inplace=True)
bay_ridge =  bay_ridge.drop('index', axis =1)

mariners_harbor = new_york[(new_york['neighbourhood_cleansed'] == 'Mariners Harbor')]
mariners_harbor.head()
mariners_harbor.reset_index(inplace=True)
mariners_harbor =  mariners_harbor.drop('index', axis =1)

williamsburg = new_york[(new_york['neighbourhood_cleansed'] == 'Williamsburg')]
williamsburg.head()
williamsburg.reset_index(inplace=True)
williamsburg =  williamsburg.drop('index', axis =1)

crown_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Crown Heights')]
crown_heights.head()
crown_heights.reset_index(inplace=True)
crown_heights =  crown_heights.drop('index', axis =1)

bensonhurst = new_york[(new_york['neighbourhood_cleansed'] == 'Bensonhurst')]
bensonhurst.head()
bensonhurst.reset_index(inplace=True)
bensonhurst =  bensonhurst.drop('index', axis =1)

south_slope = new_york[(new_york['neighbourhood_cleansed'] == 'South Slope')]
south_slope.head()
south_slope.reset_index(inplace=True)
south_slope =  south_slope.drop('index', axis =1)

bedford_stuyvesant = new_york[(new_york['neighbourhood_cleansed'] == 'Bedford-Stuyvesant')]
bedford_stuyvesant.head()
bedford_stuyvesant.reset_index(inplace=True)
bedford_stuyvesant =  bedford_stuyvesant.drop('index', axis =1)

boerum_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Boerum Hill')]
boerum_hill.head()
boerum_hill.reset_index(inplace=True)
boerum_hill =  boerum_hill.drop('index', axis =1)

kensington = new_york[(new_york['neighbourhood_cleansed'] == 'Kensington')]
kensington.head()
kensington.reset_index(inplace=True)
kensington =  kensington.drop('index', axis =1)

borough_park = new_york[(new_york['neighbourhood_cleansed'] == 'Borough Park')]
borough_park.head()
borough_park.reset_index(inplace=True)
borough_park =  borough_park.drop('index', axis =1)

bushwick = new_york[(new_york['neighbourhood_cleansed'] == 'Bushwick')]
bushwick.head()
bushwick.reset_index(inplace=True)
bushwick =  bushwick.drop('index', axis =1)

greenpoint = new_york[(new_york['neighbourhood_cleansed'] == 'Greenpoint')]
greenpoint.head()
greenpoint.reset_index(inplace=True)
greenpoint =  greenpoint.drop('index', axis =1)

coney_island = new_york[(new_york['neighbourhood_cleansed'] == 'Coney Island')]
coney_island.head()
coney_island.reset_index(inplace=True)
coney_island =  coney_island.drop('index', axis =1)

flatbush = new_york[(new_york['neighbourhood_cleansed'] == 'Flatbush')]
flatbush.head()
flatbush.reset_index(inplace=True)
flatbush =  coney_island.drop('index', axis =1)

dyker_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Dyker Heights')]
dyker_heights.head()
dyker_heights.reset_index(inplace=True)
dyker_heights =  dyker_heights.drop('index', axis =1)

sheepshead_bay = new_york[(new_york['neighbourhood_cleansed'] == 'Sheepshead Bay')]
sheepshead_bay.head()
sheepshead_bay.reset_index(inplace=True)
sheepshead_bay =  sheepshead_bay.drop('index', axis =1)

red_hook = new_york[(new_york['neighbourhood_cleansed'] == 'Red Hook')]
red_hook.head()
red_hook.reset_index(inplace=True)
red_hook =  red_hook.drop('index', axis =1)

bergen_beach = new_york[(new_york['neighbourhood_cleansed'] == 'Bergen Beach')]
bergen_beach.head()
bergen_beach.reset_index(inplace=True)
bergen_beach =  bergen_beach.drop('index', axis =1)

canarsie = new_york[(new_york['neighbourhood_cleansed'] == 'Canarsie')]
canarsie.head()
canarsie.reset_index(inplace=True)
canarsie =  canarsie.drop('index', axis =1)

prospect_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Prospect Heights')]
prospect_heights.head()
prospect_heights.reset_index(inplace=True)
prospect_heights =  prospect_heights.drop('index', axis =1)

east_flatbush = new_york[(new_york['neighbourhood_cleansed'] == 'East Flatbush')]
east_flatbush.head()
east_flatbush.reset_index(inplace=True)
east_flatbush =  east_flatbush.drop('index', axis =1)

carroll_gardens = new_york[(new_york['neighbourhood_cleansed'] == 'Carroll Gardens')]
carroll_gardens.head()
carroll_gardens.reset_index(inplace=True)
carroll_gardens = carroll_gardens.drop('index', axis =1)

fort_greene = new_york[(new_york['neighbourhood_cleansed'] == 'Fort Greene')]
fort_greene.head()
fort_greene.reset_index(inplace=True)
fort_greene = fort_greene.drop('index', axis =1)

prospect_lefferts = new_york[(new_york['neighbourhood_cleansed'] == 'Prospect-Lefferts Gardens')]
prospect_lefferts.head()
prospect_lefferts.reset_index(inplace=True)
prospect_lefferts = prospect_lefferts.drop('index', axis =1)

brighton_beach = new_york[(new_york['neighbourhood_cleansed'] == 'Brighton Beach')]
brighton_beach.head()
brighton_beach.reset_index(inplace=True)
brighton_beach = brighton_beach.drop('index', axis =1)

dumbo = new_york[(new_york['neighbourhood_cleansed'] == 'DUMBO')]
dumbo.head()
dumbo.reset_index(inplace=True)
dumbo = dumbo.drop('index', axis =1)

columbia = new_york[(new_york['neighbourhood_cleansed'] == 'Columbia St')]
columbia.head()
columbia.reset_index(inplace=True)
columbia = columbia.drop('index', axis =1)

cypress_hills = new_york[(new_york['neighbourhood_cleansed'] == 'Cypress Hills')]
cypress_hills.head()
cypress_hills.reset_index(inplace=True)
cypress_hills = cypress_hills.drop('index', axis =1)

park_slope = new_york[(new_york['neighbourhood_cleansed'] == 'Park Slope')]
park_slope.head()
park_slope.reset_index(inplace=True)
park_slope = park_slope.drop('index', axis =1)

gravesend = new_york[(new_york['neighbourhood_cleansed'] == 'Gravesend')]
gravesend.head()
gravesend.reset_index(inplace=True)
gravesend = gravesend.drop('index', axis =1)

sunset_park = new_york[(new_york['neighbourhood_cleansed'] == 'Sunset Park')]
sunset_park.head()
sunset_park.reset_index(inplace=True)
sunset_park = sunset_park.drop('index', axis =1)

boerum_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Boerum Hill')]
boerum_hill.head()
boerum_hill.reset_index(inplace=True)
boerum_hill = boerum_hill.drop('index', axis =1)

cobble_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Cobble Hill')]
cobble_hill.head()
cobble_hill.reset_index(inplace=True)
cobble_hill = cobble_hill.drop('index', axis =1)

gowanus = new_york[(new_york['neighbourhood_cleansed'] == 'Gowanus')]
gowanus.head()
gowanus.reset_index(inplace=True)
gowanus = gowanus.drop('index', axis =1)

downtown_brooklyn = new_york[(new_york['neighbourhood_cleansed'] == 'Downtown Brooklyn')]
downtown_brooklyn.head()
downtown_brooklyn.reset_index(inplace=True)
downtown_brooklyn = downtown_brooklyn.drop('index', axis =1)

bath_beach = new_york[(new_york['neighbourhood_cleansed'] == 'Bath Beach')]
bath_beach.head()
bath_beach.reset_index(inplace=True)
bath_beach = bath_beach.drop('index', axis =1)

#Bronx


pelham_bay = new_york[(new_york['neighbourhood_cleansed'] == 'Pelham Bay')]
pelham_bay.head()
pelham_bay.reset_index(inplace=True)
pelham_bay =  pelham_bay.drop('index', axis =1)

morris_park = new_york[(new_york['neighbourhood_cleansed'] == 'Morris Park')]
morris_park.head()
morris_park.reset_index(inplace=True)
morris_park =  morris_park.drop('index', axis =1)

bronxdale = new_york[(new_york['neighbourhood_cleansed'] == 'Bronxdale')]
bronxdale.head()
bronxdale.reset_index(inplace=True)
bronxdale =  bronxdale.drop('index', axis =1)

eastchester = new_york[(new_york['neighbourhood_cleansed'] == 'Eastchester')]
eastchester.head()
eastchester.reset_index(inplace=True)
eastchester =  eastchester.drop('index', axis =1)

wakefield = new_york[(new_york['neighbourhood_cleansed'] == 'Wakefield')]
wakefield.head()
wakefield.reset_index(inplace=True)
wakefield =  wakefield.drop('index', axis =1)

soundview = new_york[(new_york['neighbourhood_cleansed'] == 'Soundview')]
soundview.head()
soundview.reset_index(inplace=True)
soundview =  soundview.drop('index', axis =1)

mount_eden = new_york[(new_york['neighbourhood_cleansed'] == 'Mount Eden')]
mount_eden.head()
mount_eden.reset_index(inplace=True)
mount_eden =  mount_eden.drop('index', axis =1)

port_morris = new_york[(new_york['neighbourhood_cleansed'] == 'Port Morris')]
port_morris.head()
port_morris.reset_index(inplace=True)
port_morris =  port_morris.drop('index', axis =1)

allerton = new_york[(new_york['neighbourhood_cleansed'] == 'Allerton')]
allerton.head()
allerton.reset_index(inplace=True)
allerton =  allerton.drop('index', axis =1)

belmont = new_york[(new_york['neighbourhood_cleansed'] == 'Belmont')]
belmont.head()
belmont.reset_index(inplace=True)
belmont =  belmont.drop('index', axis =1)

st_albans = new_york[(new_york['neighbourhood_cleansed'] == 'St. Albans')]
st_albans.head()
st_albans.reset_index(inplace=True)
st_albans =  st_albans.drop('index', axis =1)

east_morrisania = new_york[(new_york['neighbourhood_cleansed'] == 'East Morrisania')]
east_morrisania.head()
east_morrisania.reset_index(inplace=True)
east_morrisania =  east_morrisania.drop('index', axis =1)

university_heights = new_york[(new_york['neighbourhood_cleansed'] == 'University Heights')]
university_heights.head()
university_heights.reset_index(inplace=True)
university_heights =  university_heights.drop('index', axis =1)

van_nest = new_york[(new_york['neighbourhood_cleansed'] == 'Van Nest')]
van_nest.head()
van_nest.reset_index(inplace=True)
van_nest =  van_nest.drop('index', axis =1)

morris_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Morris Heights')]
morris_heights.head()
morris_heights.reset_index(inplace=True)
morris_heights =  morris_heights.drop('index', axis =1)

claremont_village = new_york[(new_york['neighbourhood_cleansed'] == 'Claremont Village')]
claremont_village.head()
claremont_village.reset_index(inplace=True)
claremont_village =  claremont_village.drop('index', axis =1)

longwood = new_york[(new_york['neighbourhood_cleansed'] == 'Longwood')]
longwood.head()
longwood.reset_index(inplace=True)
longwood =  longwood.drop('index', axis =1)

clifton = new_york[(new_york['neighbourhood_cleansed'] == 'Clifton')]
clifton.head()
clifton.reset_index(inplace=True)
clifton =  clifton.drop('index', axis =1)

charleston = new_york[(new_york['neighbourhood_cleansed'] == 'Charleston')]
charleston.head()
charleston.reset_index(inplace=True)
charleston =  charleston.drop('index', axis =1)

st_george = new_york[(new_york['neighbourhood_cleansed'] == 'St. George')]
st_george.head()
st_george.reset_index(inplace=True)
st_george =  st_george.drop('index', axis =1)

windsor_terrace = new_york[(new_york['neighbourhood_cleansed'] == 'Windsor Terrace')]
windsor_terrace.head()
windsor_terrace.reset_index(inplace=True)
windsor_terrace =  windsor_terrace.drop('index', axis =1)

#Manhattan

chelsea = new_york[(new_york['neighbourhood_cleansed'] == 'Chelsea')]
chelsea.head()
chelsea.reset_index(inplace=True)
chelsea =  chelsea.drop('index', axis =1)

lower_east_side = new_york[(new_york['neighbourhood_cleansed'] == 'Lower East Side')]
lower_east_side.head()
lower_east_side.reset_index(inplace=True)
lower_east_side =  lower_east_side.drop('index', axis =1)

east_village = new_york[(new_york['neighbourhood_cleansed'] == 'East Village')]
east_village.head()
east_village.reset_index(inplace=True)
east_village =  east_village.drop('index', axis =1)

fidi = new_york[(new_york['neighbourhood_cleansed'] == 'Financial District')]
fidi.head()
fidi.reset_index(inplace=True)
fidi =  fidi.drop('index', axis =1)

flatiron = new_york[(new_york['neighbourhood_cleansed'] == 'Flatiron District')]
flatiron.head()
flatiron.reset_index(inplace=True)
flatiron =  flatiron.drop('index', axis =1)

noho = new_york[(new_york['neighbourhood_cleansed'] == 'NoHo')]
noho.head()
noho.reset_index(inplace=True)
noho =  noho.drop('index', axis =1)

soho = new_york[(new_york['neighbourhood_cleansed'] == 'SoHo')]
soho.head()
soho.reset_index(inplace=True)
soho =  soho.drop('index', axis =1)

tribeca.reset_index(inplace=True)
tribeca.head()
tribeca.reset_index(inplace=True)
tribeca =  tribeca.drop('index', axis =1)

west_village = new_york[(new_york['neighbourhood_cleansed'] == 'West Village')]
west_village.head()
west_village.reset_index(inplace=True)
west_village =  west_village.drop('index', axis =1)

murray_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Murray Hill')]
murray_hill.head()
murray_hill.reset_index(inplace=True)
murray_hill =  murray_hill.drop('index', axis =1)

upper_west = new_york[(new_york['neighbourhood_cleansed'] == 'Upper West Side')]
upper_west.head()
upper_west.reset_index(inplace=True)
upper_west =  upper_west.drop('index', axis =1)

upper_east = new_york[(new_york['neighbourhood_cleansed'] == 'Upper East Side')]
upper_east.head()
upper_east.reset_index(inplace=True)
upper_east =  upper_east.drop('index', axis =1)

midtown = new_york[(new_york['neighbourhood_cleansed'] == 'Midtown')]
midtown.head()
midtown.reset_index(inplace=True)
midtown =  midtown.drop('index', axis =1)

harlem = new_york[(new_york['neighbourhood_cleansed'] == 'Harlem')]
harlem.head()
harlem.reset_index(inplace=True)
harlem =  harlem.drop('index', axis =1)

east_harlem = new_york[(new_york['neighbourhood_cleansed'] == 'East Harlem')]
east_harlem.head()
east_harlem.reset_index(inplace=True)
east_harlem =  east_harlem.drop('index', axis =1)

washington_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Washington Heights')]
washington_heights.head()
washington_heights.reset_index(inplace=True)
washington_heights =  washington_heights.drop('index', axis =1)

theater_district = new_york[(new_york['neighbourhood_cleansed'] == 'Theater District')]
theater_district.head()
theater_district.reset_index(inplace=True)
theater_district =  theater_district.drop('index', axis =1)

hells_kitchen = new_york[(new_york['neighbourhood_cleansed'] == 'Hell\'s Kitchen')]
hells_kitchen.head()
hells_kitchen.reset_index(inplace=True)
hells_kitchen =  hells_kitchen.drop('index', axis =1)

clinton_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Clinton Hill')]
clinton_hill.head()
clinton_hill.reset_index(inplace=True)
clinton_hill =  clinton_hill.drop('index', axis =1)

roosevelt_island = new_york[(new_york['neighbourhood_cleansed'] == 'Roosevelt Island')]
roosevelt_island.head()
roosevelt_island.reset_index(inplace=True)
roosevelt_island =  roosevelt_island.drop('index', axis =1)

battery_park = new_york[(new_york['neighbourhood_cleansed'] == 'Battery Park City')]
battery_park.head()
battery_park.reset_index(inplace=True)
battery_park =  battery_park.drop('index', axis =1)

riverdale = new_york[(new_york['neighbourhood_cleansed'] == 'Riverdale')]
riverdale.head()
riverdale.reset_index(inplace=True)
riverdale =  riverdale.drop('index', axis =1)

long_island = new_york[(new_york['neighbourhood_cleansed'] == 'Long Island City')]
long_island.head()
long_island.reset_index(inplace=True)
long_island =  long_island.drop('index', axis =1)

ditmars_steinway = new_york[(new_york['neighbourhood_cleansed'] == 'Ditmars Steinway')]
ditmars_steinway.head()
ditmars_steinway.reset_index(inplace=True)
ditmars_steinway =  ditmars_steinway.drop('index', axis =1)

inwood = new_york[(new_york['neighbourhood_cleansed'] == 'Inwood')]
inwood.head()
inwood.reset_index(inplace=True)
inwood =  inwood.drop('index', axis =1)

gramercy = new_york[(new_york['neighbourhood_cleansed'] == 'Gramercy')]
gramercy.head()
gramercy.reset_index(inplace=True)
gramercy =  gramercy.drop('index', axis =1)

nolita = new_york[(new_york['neighbourhood_cleansed'] == 'Nolita')]
nolita.head()
nolita.reset_index(inplace=True)
nolita =  nolita.drop('index', axis =1)

chinatown = new_york[(new_york['neighbourhood_cleansed'] == 'Chinatown')]
chinatown.head()
chinatown.reset_index(inplace=True)
chinatown =  chinatown.drop('index', axis =1)

kips_bay = new_york[(new_york['neighbourhood_cleansed'] == 'Kips Bay')]
kips_bay.head()
kips_bay.reset_index(inplace=True)
kips_bay =  kips_bay.drop('index', axis =1)

civic_center = new_york[(new_york['neighbourhood_cleansed'] == 'Civic Center')]
civic_center.head()
civic_center.reset_index(inplace=True)
civic_center =  civic_center.drop('index', axis =1)

two_bridges = new_york[(new_york['neighbourhood_cleansed'] == 'Two Bridges')]
two_bridges.head()
two_bridges.reset_index(inplace=True)
two_bridges =  two_bridges.drop('index', axis =1)

#%%


brooklyn_s = get_stats(brooklyn)
brooklyn_s['location'] = 'Brooklyn, NY'
brooklyn_s = reorder(brooklyn_s)

bronx_s = get_stats(bronx)
bronx_s['location'] = 'Bronx, NY'
bronx_s = reorder(bronx_s)

manhattan_s = get_stats(manhattan)
manhattan_s['location'] = 'Manhattan, NY'
manhattan_s = reorder(manhattan_s)

queens_s = get_stats(queens)
queens_s['location'] = 'Queens, NY'
queens_s = reorder(queens_s)

staten_island_s = get_stats(staten_island)
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

pop = read_csv('DataScience\pop_cities_census.csv').convert_objects(convert_numeric=True)
pop.columns = ['City', 'Population']
pop = pop.set_index('City')

#Merging with listing data and normalizing
df1 = concat([df, pop], axis= 1)
df1 = df1.astype('float')
df1['Normalized by Population'] = df1['Count of Listings'] / df1['Population']
df1.sort_values(['Normalized by Population'], ascending=[False]).reset_index(0)

z = [(365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True), df1['Normalized by Population']]
df2 = concat(z, axis = 1)
df2

#Estimating Supply and Demand of Listings: Popularity and Normalized Count of Listings
#%%

z = [(365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True), df1['Normalized by Population']]
df2 = concat(z, axis = 1)

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

#Average Price per City: Where is it the most and least expensive to stay, on average, at an Airbnb listing?

DataFrame(statistics['price']['mean'].convert_objects(convert_numeric=True)).sort_values(['mean'], ascending=[False])

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

#Average Availability of Listings: What cities are more popular to vist?
#%%

x = (365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True)
x = DataFrame(x).sort_values(['mean'], ascending=[False])
x.columns = ['Availability']
x

x = DataFrame(statistics['number_of_reviews']['mean'].convert_objects(convert_numeric=True)).sort_values(['mean'], ascending=[False])
x.columns = ['Avg. # of Reviews']
x

#Price and Availibility Listings: What the relationship between populatity of a listing and its price?

#%%

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

df = concat ([x,y], axis =1 )
df.corr()

#Price and Average Rating: How does the average quality of a listing correlate to the average price?
#%%

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

#Correlation Matrix for Airbnb Listing Data: Which Airbnb metrics are related to each other and how?
#%%

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

ZHVI = read_csv('DataScience\Zip_Zhvi_Summary_AllHomes.csv', encoding = 'latin1').set_index('RegionName')

x = ['Brooklyn, NY', 'Bronx, NY', 'Queens, NY', 'Manhattan, NY', 'Staten Island, NY']
y = ['Zhvi', 'MoM', 'QoQ', 'YoY', '5Year', '10Year']

ZHVI = ZHVI.loc[x,y]

#Putting all the data into one Dataframe for correlation analysis

df_zillow = ZHVI
df_zillow.columns = ['ZHVI', 'ZHVI_MoM', 'ZHVI_QoQ', 'ZHVI_YoY', 'ZHVI_5Year', 'ZHVI_10Year']
df_zillow

# How does the median home price of a city influence the price of an Airbnb listing?

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
plt.title('Home Price (ZHVI) and Airbnb Listing Price', fontsize=20, fontweight='bold')


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

#Coorelation Matrix for ZHVI: How do ZHVI metrics relate to one another?

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

#Coorelation Matrix for ZHVI and Price: How do Listing Price and Home Value relate?

df1 = DataFrame(statistics.iloc[:,17])
df = concat([df1, df2], axis =1)
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