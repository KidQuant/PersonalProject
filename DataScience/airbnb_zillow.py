
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

new_york = read_csv('/Users/andresealy/Documents/PersonalProject/DataScience/listings.csv')    #For Mac Computers
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

east_flatbush_s = get_stats(east_flatbush)
east_flatbush_s['location'] = 'East Flatbush'
east_flatbush_s = reorder(east_flatbush_s)

bensonhurst = new_york[(new_york['neighbourhood_cleansed'] == 'Bensonhurst')]
bensonhurst.head()
bensonhurst.reset_index(inplace=True)
bensonhurst =  bensonhurst.drop('index', axis =1)

bensonhurst_s = get_stats(bensonhurst)
bensonhurst_s['location'] = 'Bensonhurst'
bensonhurst_s = reorder(bensonhurst_s)

navy_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Navy Hill')]
navy_hill.head()
navy_hill.reset_index(inplace=True)
navy_hill =  navy_hill.drop('index', axis =1)

williamsburg = new_york[(new_york['neighbourhood_cleansed'] == 'Williamsburg')]
williamsburg.head()
williamsburg.reset_index(inplace=True)
williamsburg =  williamsburg.drop('index', axis =1)

williamsburg_s = get_stats(williamsburg)
williamsburg_s['location'] = 'Williamsburg'
williamsburg_s = reorder(williamsburg_s)

city_island = new_york[(new_york['neighbourhood_cleansed'] == 'City Island')]
city_island.head()
city_island.reset_index(inplace=True)
city_island =  city_island.drop('index', axis =1)

city_island_s = get_stats(city_island)
city_island_s['location'] = 'City Island'
city_island_s = reorder(city_island_s)

bay_ridge = new_york[(new_york['neighbourhood_cleansed'] == 'Bay Ridge')]
bay_ridge.head()
bay_ridge.reset_index(inplace=True)
bay_ridge =  bay_ridge.drop('index', axis =1)

bay_ridge_s = get_stats(bay_ridge)
bay_ridge_s['location'] = 'Bay Ridge'
bay_ridge_s = reorder(bay_ridge_s)

mariners_harbor = new_york[(new_york['neighbourhood_cleansed'] == 'Mariners Harbor')]
mariners_harbor.head()
mariners_harbor.reset_index(inplace=True)
mariners_harbor =  mariners_harbor.drop('index', axis =1)

mariners_harbor_s = get_stats(mariners_harbor)
mariners_harbor_s['location'] = 'Mariners Harbor'
mariners_harbor_s = reorder(mariners_harbor_s)

crown_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Crown Heights')]
crown_heights.head()
crown_heights.reset_index(inplace=True)
crown_heights =  crown_heights.drop('index', axis =1)

crown_heights_s = get_stats(crown_heights)
crown_heights_s['location'] = 'Crown Heights'
crown_heights_s = reorder(crown_heights_s)

south_slope = new_york[(new_york['neighbourhood_cleansed'] == 'South Slope')]
south_slope.head()
south_slope.reset_index(inplace=True)
south_slope =  south_slope.drop('index', axis =1)

south_slope_s = get_stats(south_slope)
south_slope_s['location'] = 'South Slope'
south_slope_s = reorder(south_slope_s)

bedford_stuyvesant = new_york[(new_york['neighbourhood_cleansed'] == 'Bedford-Stuyvesant')]
bedford_stuyvesant.head()
bedford_stuyvesant.reset_index(inplace=True)
bedford_stuyvesant =  bedford_stuyvesant.drop('index', axis =1)

bedford_stuyvesant_s = get_stats(bedford_stuyvesant)
bedford_stuyvesant_s['location'] = 'Bedford-Stuyvesant'
bedford_stuyvesant_s = reorder(bedford_stuyvesant_s)

boerum_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Boerum Hill')]
boerum_hill.head()
boerum_hill.reset_index(inplace=True)
boerum_hill =  boerum_hill.drop('index', axis =1)

boerum_hill_s = get_stats(boerum_hill)
boerum_hill_s['location'] = 'Boerum Hill'
boerum_hill_s = reorder(boerum_hill_s)

kensington = new_york[(new_york['neighbourhood_cleansed'] == 'Kensington')]
kensington.head()
kensington.reset_index(inplace=True)
kensington =  kensington.drop('index', axis =1)

kensington_s = get_stats(kensington)
kensington_s['location'] = 'Kensington'
kensington_s = reorder(kensington_s)

borough_park = new_york[(new_york['neighbourhood_cleansed'] == 'Borough Park')]
borough_park.head()
borough_park.reset_index(inplace=True)
borough_park =  borough_park.drop('index', axis =1)

borough_park_s = get_stats(borough_park)
borough_park_s['location'] = 'Borough Park'
borough_park_s = reorder(borough_park_s)

bushwick = new_york[(new_york['neighbourhood_cleansed'] == 'Bushwick')]
bushwick.head()
bushwick.reset_index(inplace=True)
bushwick =  bushwick.drop('index', axis =1)

bushwick_s = get_stats(bushwick)
bushwick_s['location'] = 'Bushwick'
bushwick_s = reorder(bushwick_s)

greenpoint = new_york[(new_york['neighbourhood_cleansed'] == 'Greenpoint')]
greenpoint.head()
greenpoint.reset_index(inplace=True)
greenpoint =  greenpoint.drop('index', axis =1)

greenpoint_s = get_stats(greenpoint)
greenpoint_s['location'] = 'Greenpoint'
greenpoint_s = reorder(greenpoint_s)

coney_island = new_york[(new_york['neighbourhood_cleansed'] == 'Coney Island')]
coney_island.head()
coney_island.reset_index(inplace=True)
coney_island =  coney_island.drop('index', axis =1)

coney_island_s = get_stats(coney_island)
coney_island_s['location'] = 'Coney Island'
coney_island_s = reorder(coney_island_s)


flatbush = new_york[(new_york['neighbourhood_cleansed'] == 'Flatbush')]
flatbush.head()
flatbush.reset_index(inplace=True)
flatbush =  flatbush.drop('index', axis =1)

flatbush_s = get_stats(flatbush)
flatbush_s['location'] = 'Flatbush'
flatbush_s = reorder(flatbush_s)

dyker_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Dyker Heights')]
dyker_heights.head()
dyker_heights.reset_index(inplace=True)
dyker_heights =  dyker_heights.drop('index', axis =1)

dyker_heights_s = get_stats(dyker_heights)
dyker_heights_s['location'] = 'Dyker Heights'
dyker_heights_s = reorder(dyker_heights_s)

sheepshead_bay = new_york[(new_york['neighbourhood_cleansed'] == 'Sheepshead Bay')]
sheepshead_bay.head()
sheepshead_bay.reset_index(inplace=True)
sheepshead_bay =  sheepshead_bay.drop('index', axis =1)

sheepshead_bay_s = get_stats(sheepshead_bay)
sheepshead_bay_s['location'] = 'Sheepshead Bay'
sheepshead_bay_s = reorder(sheepshead_bay_s)

red_hook = new_york[(new_york['neighbourhood_cleansed'] == 'Red Hook')]
red_hook.head()
red_hook.reset_index(inplace=True)
red_hook =  red_hook.drop('index', axis =1)

red_hook_s = get_stats(red_hook)
red_hook_s['location'] = 'Red Hook'
red_hook_s = reorder(red_hook_s)

bergen_beach = new_york[(new_york['neighbourhood_cleansed'] == 'Bergen Beach')]
bergen_beach.head()
bergen_beach.reset_index(inplace=True)
bergen_beach =  bergen_beach.drop('index', axis =1)

bergen_beach_s = get_stats(bergen_beach)
bergen_beach_s['location'] = 'Bergen Beach'
bergen_beach_s = reorder(bergen_beach_s)

canarsie = new_york[(new_york['neighbourhood_cleansed'] == 'Canarsie')]
canarsie.head()
canarsie.reset_index(inplace=True)
canarsie =  canarsie.drop('index', axis =1)

canarsie_s = get_stats(canarsie)
canarsie_s['location'] = 'Canarsie'
canarsie_s = reorder(canarsie_s)

prospect_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Prospect Heights')]
prospect_heights.head()
prospect_heights.reset_index(inplace=True)
prospect_heights =  prospect_heights.drop('index', axis =1)

prospect_heights_s = get_stats(prospect_heights)
prospect_heights_s['location'] = 'Prospect Heights'
prospect_heights_s = reorder(prospect_heights_s)

east_flatbush = new_york[(new_york['neighbourhood_cleansed'] == 'East Flatbush')]
east_flatbush.head()
east_flatbush.reset_index(inplace=True)
east_flatbush =  east_flatbush.drop('index', axis =1)

east_flatbush_s = get_stats(east_flatbush)
east_flatbush_s['location'] = 'East Flatbush'
east_flatbush_s = reorder(east_flatbush_s)

carroll_gardens = new_york[(new_york['neighbourhood_cleansed'] == 'Carroll Gardens')]
carroll_gardens.head()
carroll_gardens.reset_index(inplace=True)
carroll_gardens = carroll_gardens.drop('index', axis =1)

carroll_gardens_s = get_stats(carroll_gardens)
carroll_gardens_s['location'] = 'Carroll Gardens'
carroll_gardens_s = reorder(carroll_gardens_s)

fort_greene = new_york[(new_york['neighbourhood_cleansed'] == 'Fort Greene')]
fort_greene.head()
fort_greene.reset_index(inplace=True)
fort_greene = fort_greene.drop('index', axis =1)

fort_greene_s = get_stats(fort_greene)
fort_greene_s['location'] = 'Fort Greene'
fort_greene_s = reorder(fort_greene_s)

prospect_lefferts = new_york[(new_york['neighbourhood_cleansed'] == 'Prospect-Lefferts Gardens')]
prospect_lefferts.head()
prospect_lefferts.reset_index(inplace=True)
prospect_lefferts = prospect_lefferts.drop('index', axis =1)

prospect_heights_s = get_stats(prospect_heights)
prospect_heights_s['location'] = 'Prospect-Lefferts Gardens'
prospect_heights_s = reorder(prospect_heights_s)

brighton_beach = new_york[(new_york['neighbourhood_cleansed'] == 'Brighton Beach')]
brighton_beach.head()
brighton_beach.reset_index(inplace=True)
brighton_beach = brighton_beach.drop('index', axis =1)

brighton_beach_s = get_stats(brighton_beach)
brighton_beach_s['location'] = 'Brighton Beach'
brighton_beach_s = reorder(brighton_beach_s)

dumbo = new_york[(new_york['neighbourhood_cleansed'] == 'DUMBO')]
dumbo.head()
dumbo.reset_index(inplace=True)
dumbo = dumbo.drop('index', axis =1)

dumbo_s = get_stats(dumbo)
dumbo_s['location'] = 'DUMBO'
dumbo_s = reorder(dumbo_s)

columbia = new_york[(new_york['neighbourhood_cleansed'] == 'Columbia St')]
columbia.head()
columbia.reset_index(inplace=True)
columbia = columbia.drop('index', axis =1)

columbia_s = get_stats(columbia)
columbia_s['location'] = 'Columbia St'
columbia_s = reorder(columbia_s)

cypress_hills = new_york[(new_york['neighbourhood_cleansed'] == 'Cypress Hills')]
cypress_hills.head()
cypress_hills.reset_index(inplace=True)
cypress_hills = cypress_hills.drop('index', axis =1)

cypress_hills_s = get_stats(cypress_hills)
cypress_hills_s['location'] = 'Cypress Hills'
cypress_hills_s = reorder(cypress_hills_s)

park_slope = new_york[(new_york['neighbourhood_cleansed'] == 'Park Slope')]
park_slope.head()
park_slope.reset_index(inplace=True)
park_slope = park_slope.drop('index', axis =1)

park_slope_s = get_stats(park_slope)
park_slope_s['location'] = 'Park Slope'
park_slope_s = reorder(park_slope_s)

gravesend = new_york[(new_york['neighbourhood_cleansed'] == 'Gravesend')]
gravesend.head()
gravesend.reset_index(inplace=True)
gravesend = gravesend.drop('index', axis =1)

gravesend_s = get_stats(gravesend)
gravesend_s['location'] = 'Gravesend'
gravesend_s = reorder(gravesend_s)

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

tribeca = new_york[(new_york['neighbourhood_cleansed'] == 'Tribeca')]
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

#Queens

glen_oaks = new_york[(new_york['neighbourhood_cleansed'] == 'Glen Oaks')]
glen_oaks.head()
glen_oaks.reset_index(inplace=True)
glen_oaks =  glen_oaks.drop('index', axis =1)

sunnyside = new_york[(new_york['neighbourhood_cleansed'] == 'Sunnyside')]
sunnyside.head()
sunnyside.reset_index(inplace=True)
sunnyside =  sunnyside.drop('index', axis =1)

astoria = new_york[(new_york['neighbourhood_cleansed'] == 'Astoria')]
astoria.head()
astoria.reset_index(inplace=True)
astoria =  astoria.drop('index', axis =1)

flushing = new_york[(new_york['neighbourhood_cleansed'] == 'Flushing')]
flushing.head()
flushing.reset_index(inplace=True)
flushing =  flushing.drop('index', axis =1)

college_point = new_york[(new_york['neighbourhood_cleansed'] == 'College Point')]
college_point.head()
college_point.reset_index(inplace=True)
college_point =  college_point.drop('index', axis =1)

whitestone = new_york[(new_york['neighbourhood_cleansed'] == 'Whitestone')]
whitestone.head()
whitestone.reset_index(inplace=True)
whitestone =  whitestone.drop('index', axis =1)

bayside = new_york[(new_york['neighbourhood_cleansed'] == 'Bayside')]
bayside.head()
bayside.reset_index(inplace=True)
bayside =  bayside.drop('index', axis =1)

little_neck = new_york[(new_york['neighbourhood_cleansed'] == 'Little Neck')]
little_neck.head()
little_neck.reset_index(inplace=True)
little_neck =  little_neck.drop('index', axis =1)

fresh_meadows = new_york[(new_york['neighbourhood_cleansed'] == 'Fresh Meadows')]
fresh_meadows.head()
fresh_meadows.reset_index(inplace=True)
fresh_meadows =  fresh_meadows.drop('index', axis =1)

corona = new_york[(new_york['neighbourhood_cleansed'] == 'Corona')]
corona.head()
corona.reset_index(inplace=True)
corona =  corona.drop('index', axis =1)

east_elmhurst = new_york[(new_york['neighbourhood_cleansed'] == 'East Elmhurst')]
east_elmhurst.head()
east_elmhurst.reset_index(inplace=True)
east_elmhurst =  east_elmhurst.drop('index', axis =1)

jackson_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Jackson Heights')]
jackson_heights.head()
jackson_heights.reset_index(inplace=True)
jackson_heights =  jackson_heights.drop('index', axis =1)

forest_hills = new_york[(new_york['neighbourhood_cleansed'] == 'Forest Hills')]
forest_hills.head()
forest_hills.reset_index(inplace=True)
forest_hills =  forest_hills.drop('index', axis =1)

woodside = new_york[(new_york['neighbourhood_cleansed'] == 'Woodside')]
woodside.head()
woodside.reset_index(inplace=True)
woodside =  woodside.drop('index', axis =1)

maspeth = new_york[(new_york['neighbourhood_cleansed'] == 'Maspeth')]
maspeth.head()
maspeth.reset_index(inplace=True)
maspeth =  maspeth.drop('index', axis =1)

middle_village = new_york[(new_york['neighbourhood_cleansed'] == 'Middle Village')]
middle_village.head()
middle_village.reset_index(inplace=True)
middle_village =  middle_village.drop('index', axis =1)

ridgewood = new_york[(new_york['neighbourhood_cleansed'] == 'Ridgewood')]
ridgewood.head()
ridgewood.reset_index(inplace=True)
ridgewood =  ridgewood.drop('index', axis =1)

cambria_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Cambria Heights')]
cambria_heights.head()
cambria_heights.reset_index(inplace=True)
cambria_heights =  cambria_heights.drop('index', axis =1)

springfield = new_york[(new_york['neighbourhood_cleansed'] == 'Springfield Gardens')]
springfield.head()
springfield.reset_index(inplace=True)
springfield =  springfield.drop('index', axis =1)

howard_beach = new_york[(new_york['neighbourhood_cleansed'] == 'Howard Beach')]
howard_beach.head()
howard_beach.reset_index(inplace=True)
howard_beach =  howard_beach.drop('index', axis =1)

kew_gardens = new_york[(new_york['neighbourhood_cleansed'] == 'Kew Gardens')]
kew_gardens.head()
kew_gardens.reset_index(inplace=True)
kew_gardens =  kew_gardens.drop('index', axis =1)

ozone = new_york[(new_york['neighbourhood_cleansed'] == 'Ozone Park')]
ozone.head()
ozone.reset_index(inplace=True)
ozone =  ozone.drop('index', axis =1)

richmond_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Richmond Hill')]
richmond_hill.head()
richmond_hill.reset_index(inplace=True)
richmond_hill =  richmond_hill.drop('index', axis =1)

south_ozone_park = new_york[(new_york['neighbourhood_cleansed'] == 'South Ozone Park')]
south_ozone_park.head()
south_ozone_park.reset_index(inplace=True)
south_ozone_park =  south_ozone_park.drop('index', axis =1)

woodhaven = new_york[(new_york['neighbourhood_cleansed'] == 'Woodhaven')]
woodhaven.head()
woodhaven.reset_index(inplace=True)
woodhaven =  woodhaven.drop('index', axis =1)

rosedale = new_york[(new_york['neighbourhood_cleansed'] == 'Rosedale')]
rosedale.head()
rosedale.reset_index(inplace=True)
rosedale =  rosedale.drop('index', axis =1)

hollis = new_york[(new_york['neighbourhood_cleansed'] == 'Hollis')]
hollis.head()
hollis.reset_index(inplace=True)
hollis =  hollis.drop('index', axis =1)

bellerose = new_york[(new_york['neighbourhood_cleansed'] == 'Bellerose')]
bellerose.head()
bellerose.reset_index(inplace=True)
bellerose = bellerose.drop('index', axis =1)

queens_village = new_york[(new_york['neighbourhood_cleansed'] == 'Queens Village')]
queens_village.head()
queens_village.reset_index(inplace=True)
queens_village = queens_village.drop('index', axis =1)

jamaica = new_york[(new_york['neighbourhood_cleansed'] == 'Jamaica')]
jamaica.head()
jamaica.reset_index(inplace=True)
jamaica = jamaica.drop('index', axis =1)

edgemere = new_york[(new_york['neighbourhood_cleansed'] == 'Edgemere')]
edgemere.head()
edgemere.reset_index(inplace=True)
edgemere = edgemere.drop('index', axis =1)

elmhurst = new_york[(new_york['neighbourhood_cleansed'] == 'Elmhurst')]
elmhurst.head()
elmhurst.reset_index(inplace=True)
elmhurst = elmhurst.drop('index', axis =1)

rego_park = new_york[(new_york['neighbourhood_cleansed'] == 'Rego Park')]
rego_park.head()
rego_park.reset_index(inplace=True)
rego_park = rego_park.drop('index', axis =1)

glendale = new_york[(new_york['neighbourhood_cleansed'] == 'Glendale')]
glendale.head()
glendale.reset_index(inplace=True)
glendale = glendale.drop('index', axis =1)

southozone = new_york[(new_york['neighbourhood_cleansed'] == 'South Ozone Park')]
southozone.head()
southozone.reset_index(inplace=True)
southozone = southozone.drop('index', axis =1)

#Staten Island

silver_lake = new_york[(new_york['neighbourhood_cleansed'] == 'Silver Lake')]
silver_lake.head()
silver_lake.reset_index(inplace=True)
silver_lake = silver_lake.drop('index', axis =1)

west_brighton = new_york[(new_york['neighbourhood_cleansed'] == 'West Brighton')]
west_brighton.head()
west_brighton.reset_index(inplace=True)
west_brighton = west_brighton.drop('index', axis =1)

grymes_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Grymes Hill')]
grymes_hill.head()
grymes_hill.reset_index(inplace=True)
grymes_hill = grymes_hill.drop('index', axis =1)

great_kills = new_york[(new_york['neighbourhood_cleansed'] == 'Great Kills')]
great_kills.head()
great_kills.reset_index(inplace=True)
great_kills = great_kills.drop('index', axis =1)

rosebank = new_york[(new_york['neighbourhood_cleansed'] == 'Rosebank')]
rosebank.head()
rosebank.reset_index(inplace=True)
rosebank = rosebank.drop('index', axis =1)

tottenville = new_york[(new_york['neighbourhood_cleansed'] == 'Tottenville')]
tottenville.head()
tottenville.reset_index(inplace=True)
tottenville = tottenville.drop('index', axis =1)

rossville = new_york[(new_york['neighbourhood_cleansed'] == 'Rossville')]
rossville.head()
rossville.reset_index(inplace=True)
rossville = rossville.drop('index', axis =1)

west_brighton = new_york[(new_york['neighbourhood_cleansed'] == 'West Brighton')]
west_brighton.head()
west_brighton.reset_index(inplace=True)
west_brighton = west_brighton.drop('index', axis =1)

bull_head = new_york[(new_york['neighbourhood_cleansed'] == 'Bull\'s Head')]
bull_head.head()
bull_head.reset_index(inplace=True)
bull_head = bull_head.drop('index', axis =1)

randall_manor = new_york[(new_york['neighbourhood_cleansed'] == 'Randall Manor')]
randall_manor.head()
randall_manor.reset_index(inplace=True)
randall_manor = randall_manor.drop('index', axis =1)

# Extracting the statistics

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

#%%
austin_s = get_stats(austin)
austin_s['location'] = 'Austin, TX'
austin_s = reorder(austin_s)


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
