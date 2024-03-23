
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

#%% Brooklyn

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

prospect_lefferts_s = get_stats(prospect_lefferts)
prospect_lefferts_s['location'] = 'Prospect-Lefferts Gardens'
prospect_lefferts_s = reorder(prospect_lefferts_s)

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

sunset_park_s = get_stats(sunset_park)
sunset_park_s['location'] = 'Sunset Park'
sunset_park_s = reorder(sunset_park_s)

cobble_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Cobble Hill')]
cobble_hill.head()
cobble_hill.reset_index(inplace=True)
cobble_hill = cobble_hill.drop('index', axis =1)

cobble_hill_s = get_stats(cobble_hill)
cobble_hill_s['location'] = 'Cobble Hill'
cobble_hill_s = reorder(cobble_hill_s)

gowanus = new_york[(new_york['neighbourhood_cleansed'] == 'Gowanus')]
gowanus.head()
gowanus.reset_index(inplace=True)
gowanus = gowanus.drop('index', axis =1)

gowanus_s = get_stats(gowanus)
gowanus_s['location'] = 'Gowanus'
gowanus_s = reorder(gowanus_s)

downtown_brooklyn = new_york[(new_york['neighbourhood_cleansed'] == 'Downtown Brooklyn')]
downtown_brooklyn.head()
downtown_brooklyn.reset_index(inplace=True)
downtown_brooklyn = downtown_brooklyn.drop('index', axis =1)

downtown_brooklyn_s = get_stats(downtown_brooklyn)
downtown_brooklyn_s['location'] = 'Downtown Brooklyn'
downtown_brooklyn_s = reorder(downtown_brooklyn_s)

bath_beach = new_york[(new_york['neighbourhood_cleansed'] == 'Bath Beach')]
bath_beach.head()
bath_beach.reset_index(inplace=True)
bath_beach = bath_beach.drop('index', axis =1)

bath_beach_s = get_stats(bath_beach)
bath_beach_s['location'] = 'Bath Beach'
bath_beach_s = reorder(bath_beach_s)

#%%
#Bronx

pelham_bay = new_york[(new_york['neighbourhood_cleansed'] == 'Pelham Bay')]
pelham_bay.head()
pelham_bay.reset_index(inplace=True)
pelham_bay =  pelham_bay.drop('index', axis =1)

pelham_bay_s = get_stats(pelham_bay)
pelham_bay_s['location'] = 'Pelham Bay'
pelham_bay_s = reorder(pelham_bay_s)

morris_park = new_york[(new_york['neighbourhood_cleansed'] == 'Morris Park')]
morris_park.head()
morris_park.reset_index(inplace=True)
morris_park =  morris_park.drop('index', axis =1)

morris_park_s = get_stats(morris_park)
morris_park_s['location'] = 'Morris Park'
morris_park_s = reorder(morris_park_s)

bronxdale = new_york[(new_york['neighbourhood_cleansed'] == 'Bronxdale')]
bronxdale.head()
bronxdale.reset_index(inplace=True)
bronxdale =  bronxdale.drop('index', axis =1)

bronxdale_s = get_stats(bronxdale)
bronxdale_s['location'] = 'Bronxdale'
bronxdale_s = reorder(bronxdale_s)

eastchester = new_york[(new_york['neighbourhood_cleansed'] == 'Eastchester')]
eastchester.head()
eastchester.reset_index(inplace=True)
eastchester =  eastchester.drop('index', axis =1)

eastchester_s = get_stats(eastchester)
eastchester_s['location'] = 'Eastchester'
eastchester_s = reorder(eastchester_s)

wakefield = new_york[(new_york['neighbourhood_cleansed'] == 'Wakefield')]
wakefield.head()
wakefield.reset_index(inplace=True)
wakefield =  wakefield.drop('index', axis =1)

wakefield_s = get_stats(wakefield)
wakefield_s['location'] = 'Wakefield'
wakefield_s = reorder(wakefield_s)

kingsbridge = new_york[(new_york['neighbourhood_cleansed'] == 'Kingsbridge')]
kingsbridge.head()
kingsbridge.reset_index(inplace=True)
kingsbridge =  kingsbridge.drop('index', axis =1)

kingsbridge_s = get_stats(kingsbridge)
kingsbridge_s['location'] = 'Kingsbridge'
kingsbridge_s = reorder(kingsbridge_s)

pelham_gardens = new_york[(new_york['neighbourhood_cleansed'] == 'Pelham Gardens')]
pelham_gardens.head()
pelham_gardens.reset_index(inplace=True)
pelham_gardens =  pelham_gardens.drop('index', axis =1)

pelham_gardens_s = get_stats(pelham_gardens)
pelham_gardens_s['location'] = 'Pelham Gardens'
pelham_gardens_s = reorder(pelham_gardens_s)

fieldston = new_york[(new_york['neighbourhood_cleansed'] == 'Fieldston')]
fieldston.head()
fieldston.reset_index(inplace=True)
fieldston =  fieldston.drop('index', axis =1)

fieldston_s = get_stats(fieldston)
fieldston_s['location'] = 'Fieldstong'
fieldston_s = reorder(fieldston_s)


soundview = new_york[(new_york['neighbourhood_cleansed'] == 'Soundview')]
soundview.head()
soundview.reset_index(inplace=True)
soundview =  soundview.drop('index', axis =1)

soundview_s = get_stats(soundview)
soundview_s['location'] = 'Soundview'
soundview_s = reorder(soundview_s)

mount_eden = new_york[(new_york['neighbourhood_cleansed'] == 'Mount Eden')]
mount_eden.head()
mount_eden.reset_index(inplace=True)
mount_eden =  mount_eden.drop('index', axis =1)

mount_eden_s = get_stats(mount_eden)
mount_eden_s['location'] = 'Mount Eden'
mount_eden_s = reorder(mount_eden_s)

port_morris = new_york[(new_york['neighbourhood_cleansed'] == 'Port Morris')]
port_morris.head()
port_morris.reset_index(inplace=True)
port_morris =  port_morris.drop('index', axis =1)

port_morris_s = get_stats(port_morris)
port_morris_s['location'] = 'Port Morris'
port_morris_s = reorder(port_morris_s)

allerton = new_york[(new_york['neighbourhood_cleansed'] == 'Allerton')]
allerton.head()
allerton.reset_index(inplace=True)
allerton =  allerton.drop('index', axis =1)

allerton_s = get_stats(allerton)
allerton_s['location'] = 'Allerton'
allerton_s = reorder(allerton_s)

belmont = new_york[(new_york['neighbourhood_cleansed'] == 'Belmont')]
belmont.head()
belmont.reset_index(inplace=True)
belmont =  belmont.drop('index', axis =1)

belmont_s = get_stats(belmont)
belmont_s['location'] = 'Belmont'
belmont_s = reorder(belmont_s)

st_albans = new_york[(new_york['neighbourhood_cleansed'] == 'St. Albans')]
st_albans.head()
st_albans.reset_index(inplace=True)
st_albans =  st_albans.drop('index', axis =1)

st_albans_s = get_stats(st_albans)
st_albans_s['location'] = 'St. Albans'
st_albans_s = reorder(st_albans_s)

east_morrisania = new_york[(new_york['neighbourhood_cleansed'] == 'East Morrisania')]
east_morrisania.head()
east_morrisania.reset_index(inplace=True)
east_morrisania =  east_morrisania.drop('index', axis =1)

east_morrisania_s = get_stats(east_morrisania)
east_morrisania_s['location'] = 'East Morrisania'
east_morrisania_s = reorder(east_morrisania_s)

university_heights = new_york[(new_york['neighbourhood_cleansed'] == 'University Heights')]
university_heights.head()
university_heights.reset_index(inplace=True)
university_heights =  university_heights.drop('index', axis =1)

university_heights_s = get_stats(university_heights)
university_heights_s['location'] = 'University Heights'
university_heights_s = reorder(university_heights_s)

van_nest = new_york[(new_york['neighbourhood_cleansed'] == 'Van Nest')]
van_nest.head()
van_nest.reset_index(inplace=True)
van_nest =  van_nest.drop('index', axis =1)

van_nest_s = get_stats(van_nest)
van_nest_s['location'] = 'Van Nest'
van_nest_s = reorder(van_nest_s)

morris_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Morris Heights')]
morris_heights.head()
morris_heights.reset_index(inplace=True)
morris_heights =  morris_heights.drop('index', axis =1)

morris_heights_s = get_stats(morris_heights)
morris_heights_s['location'] = 'Morris Heights'
morris_heights_s = reorder(morris_heights_s)

claremont_village = new_york[(new_york['neighbourhood_cleansed'] == 'Claremont Village')]
claremont_village.head()
claremont_village.reset_index(inplace=True)
claremont_village =  claremont_village.drop('index', axis =1)

claremont_village_s = get_stats(claremont_village)
claremont_village_s['location'] = 'Claremont Village'
claremont_village_s = reorder(claremont_village_s)

longwood = new_york[(new_york['neighbourhood_cleansed'] == 'Longwood')]
longwood.head()
longwood.reset_index(inplace=True)
longwood =  longwood.drop('index', axis =1)

longwood_s = get_stats(longwood)
longwood_s['location'] = 'Longwood'
longwood_s = reorder(longwood_s)

clifton = new_york[(new_york['neighbourhood_cleansed'] == 'Clifton')]
clifton.head()
clifton.reset_index(inplace=True)
clifton =  clifton.drop('index', axis =1)

clifton_s = get_stats(clifton)
clifton_s['location'] = 'Clifton'
clifton_s = reorder(clifton_s)

charleston = new_york[(new_york['neighbourhood_cleansed'] == 'Charleston')]
charleston.head()
charleston.reset_index(inplace=True)
charleston =  charleston.drop('index', axis =1)

charleston_s = get_stats(charleston)
charleston_s['location'] = 'Charleston'
charleston_s = reorder(charleston_s)

st_george = new_york[(new_york['neighbourhood_cleansed'] == 'St. George')]
st_george.head()
st_george.reset_index(inplace=True)
st_george =  st_george.drop('index', axis =1)

st_george_s = get_stats(st_george)
st_george_s['location'] = 'St. George'
st_george_s = reorder(st_george_s)

windsor_terrace = new_york[(new_york['neighbourhood_cleansed'] == 'Windsor Terrace')]
windsor_terrace.head()
windsor_terrace.reset_index(inplace=True)
windsor_terrace =  windsor_terrace.drop('index', axis =1)

windsor_terrace_s = get_stats(windsor_terrace)
windsor_terrace_s['location'] = 'Windsor Terrance'
windsor_terrace_s = reorder(windsor_terrace_s)

#%%
#Manhattan

chelsea = new_york[(new_york['neighbourhood_cleansed'] == 'Chelsea')]
chelsea.head()
chelsea.reset_index(inplace=True)
chelsea =  chelsea.drop('index', axis =1)

chelsea_s = get_stats(chelsea)
chelsea_s['location'] = 'Chelsea'
chelsea_s = reorder(chelsea_s)

lower_east_side = new_york[(new_york['neighbourhood_cleansed'] == 'Lower East Side')]
lower_east_side.head()
lower_east_side.reset_index(inplace=True)
lower_east_side =  lower_east_side.drop('index', axis =1)

lower_east_side_s = get_stats(lower_east_side)
lower_east_side_s['location'] = 'Lower East Side'
lower_east_side_s = reorder(lower_east_side_s)

east_village = new_york[(new_york['neighbourhood_cleansed'] == 'East Village')]
east_village.head()
east_village.reset_index(inplace=True)
east_village =  east_village.drop('index', axis =1)

east_village_s = get_stats(east_village)
east_village_s['location'] = 'East Village'
east_village_s = reorder(east_village_s)

fidi = new_york[(new_york['neighbourhood_cleansed'] == 'Financial District')]
fidi.head()
fidi.reset_index(inplace=True)
fidi =  fidi.drop('index', axis =1)

fidi_s = get_stats(fidi)
fidi_s['location'] = 'Financial District'
fidi_s = reorder(fidi_s)

flatiron = new_york[(new_york['neighbourhood_cleansed'] == 'Flatiron District')]
flatiron.head()
flatiron.reset_index(inplace=True)
flatiron =  flatiron.drop('index', axis =1)

flatiron_s = get_stats(flatiron)
flatiron_s['location'] = 'Flatiron District'
flatiron_s = reorder(flatiron_s)

noho = new_york[(new_york['neighbourhood_cleansed'] == 'NoHo')]
noho.head()
noho.reset_index(inplace=True)
noho =  noho.drop('index', axis =1)

noho_s = get_stats(noho)
noho_s['location'] = 'NoHo'
noho_s = reorder(noho_s)

soho = new_york[(new_york['neighbourhood_cleansed'] == 'SoHo')]
soho.head()
soho.reset_index(inplace=True)
soho =  soho.drop('index', axis =1)

soho_s = get_stats(soho)
soho_s['location'] = 'SoHo'
soho_s = reorder(soho_s)

tribeca = new_york[(new_york['neighbourhood_cleansed'] == 'Tribeca')]
tribeca.head()
tribeca.reset_index(inplace=True)
tribeca =  tribeca.drop('index', axis =1)

tribeca_s = get_stats(tribeca)
tribeca_s['location'] = 'Tribeca'
tribeca_s = reorder(tribeca_s)

west_village = new_york[(new_york['neighbourhood_cleansed'] == 'West Village')]
west_village.head()
west_village.reset_index(inplace=True)
west_village =  west_village.drop('index', axis =1)

west_village_s = get_stats(west_village)
west_village_s['location'] = 'West Village'
west_village_s = reorder(west_village_s)

murray_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Murray Hill')]
murray_hill.head()
murray_hill.reset_index(inplace=True)
murray_hill =  murray_hill.drop('index', axis =1)

murray_hill_s = get_stats(murray_hill)
murray_hill_s['location'] = 'Murray Hill'
murray_hill_s = reorder(murray_hill_s)

upper_west = new_york[(new_york['neighbourhood_cleansed'] == 'Upper West Side')]
upper_west.head()
upper_west.reset_index(inplace=True)
upper_west =  upper_west.drop('index', axis =1)

upper_west_s = get_stats(upper_west)
upper_west_s['location'] = 'Upper West Side'
upper_west_s = reorder(upper_west_s)

upper_east = new_york[(new_york['neighbourhood_cleansed'] == 'Upper East Side')]
upper_east.head()
upper_east.reset_index(inplace=True)
upper_east =  upper_east.drop('index', axis =1)

upper_east_s = get_stats(upper_east)
upper_east_s['location'] = 'Upper East Side'
upper_east_s = reorder(upper_east_s)

midtown = new_york[(new_york['neighbourhood_cleansed'] == 'Midtown')]
midtown.head()
midtown.reset_index(inplace=True)
midtown =  midtown.drop('index', axis =1)

midtown_s = get_stats(midtown)
midtown_s['location'] = 'Midtown'
midtown_s = reorder(midtown_s)

harlem = new_york[(new_york['neighbourhood_cleansed'] == 'Harlem')]
harlem.head()
harlem.reset_index(inplace=True)
harlem =  harlem.drop('index', axis =1)

harlem_s = get_stats(harlem)
harlem_s['location'] = 'Harlem'
harlem_s = reorder(harlem_s)

east_harlem = new_york[(new_york['neighbourhood_cleansed'] == 'East Harlem')]
east_harlem.head()
east_harlem.reset_index(inplace=True)
east_harlem =  east_harlem.drop('index', axis =1)

east_harlem_s = get_stats(east_harlem)
east_harlem_s['location'] = 'East Harlem'
east_harlem_s = reorder(east_harlem_s)

washington_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Washington Heights')]
washington_heights.head()
washington_heights.reset_index(inplace=True)
washington_heights =  washington_heights.drop('index', axis =1)

washington_heights_s = get_stats(washington_heights)
washington_heights_s['location'] = 'Washington Heights'
washington_heights_s = reorder(washington_heights_s)

theater_district = new_york[(new_york['neighbourhood_cleansed'] == 'Theater District')]
theater_district.head()
theater_district.reset_index(inplace=True)
theater_district =  theater_district.drop('index', axis =1)

theater_district_s = get_stats(theater_district)
theater_district_s['location'] = 'Theater District'
theater_district_s = reorder(theater_district_s)

hells_kitchen = new_york[(new_york['neighbourhood_cleansed'] == f"Hell's Kitchen")]
hells_kitchen.head()
hells_kitchen.reset_index(inplace=True)
hells_kitchen =  hells_kitchen.drop('index', axis =1)

hells_kitchen_s = get_stats(hells_kitchen)
hells_kitchen_s['location'] = f"Hell's Kitchen"
hells_kitchen_s = reorder(hells_kitchen_s)

clinton_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Clinton Hill')]
clinton_hill.head()
clinton_hill.reset_index(inplace=True)
clinton_hill =  clinton_hill.drop('index', axis =1)

clinton_hill_s = get_stats(clinton_hill)
clinton_hill_s['location'] = 'Clinton Hill'
clinton_hill_s = reorder(clinton_hill_s)

roosevelt_island = new_york[(new_york['neighbourhood_cleansed'] == 'Roosevelt Island')]
roosevelt_island.head()
roosevelt_island.reset_index(inplace=True)
roosevelt_island =  roosevelt_island.drop('index', axis =1)

roosevelt_island_s = get_stats(roosevelt_island)
roosevelt_island_s['location'] = 'Roosevelt Island'
roosevelt_island_s = reorder(roosevelt_island_s)

battery_park = new_york[(new_york['neighbourhood_cleansed'] == 'Battery Park City')]
battery_park.head()
battery_park.reset_index(inplace=True)
battery_park =  battery_park.drop('index', axis =1)

battery_park_s = get_stats(battery_park)
battery_park_s['location'] = 'Battery Park City'
battery_park_s = reorder(battery_park_s)

riverdale = new_york[(new_york['neighbourhood_cleansed'] == 'Riverdale')]
riverdale.head()
riverdale.reset_index(inplace=True)
riverdale =  riverdale.drop('index', axis =1)

riverdale_s = get_stats(riverdale)
riverdale_s['location'] = 'Riverdale'
riverdale_s = reorder(riverdale_s)

inwood = new_york[(new_york['neighbourhood_cleansed'] == 'Inwood')]
inwood.head()
inwood.reset_index(inplace=True)
inwood =  inwood.drop('index', axis =1)

inwood_s = get_stats(inwood)
inwood_s['location'] = 'Inwood'
inwood_s = reorder(inwood_s)

gramercy = new_york[(new_york['neighbourhood_cleansed'] == 'Gramercy')]
gramercy.head()
gramercy.reset_index(inplace=True)
gramercy =  gramercy.drop('index', axis =1)

gramercy_s = get_stats(gramercy)
gramercy_s['location'] = 'Gramercy'
gramercy_s = reorder(gramercy_s)

nolita = new_york[(new_york['neighbourhood_cleansed'] == 'Nolita')]
nolita.head()
nolita.reset_index(inplace=True)
nolita =  nolita.drop('index', axis =1)

nolita_s = get_stats(nolita)
nolita_s['location'] = 'Nolita'
nolita_s = reorder(nolita_s)

chinatown = new_york[(new_york['neighbourhood_cleansed'] == 'Chinatown')]
chinatown.head()
chinatown.reset_index(inplace=True)
chinatown =  chinatown.drop('index', axis =1)

chinatown_s = get_stats(chinatown)
chinatown_s['location'] = 'Chinatown'
chinatown_s = reorder(chinatown_s)

kips_bay = new_york[(new_york['neighbourhood_cleansed'] == 'Kips Bay')]
kips_bay.head()
kips_bay.reset_index(inplace=True)
kips_bay =  kips_bay.drop('index', axis =1)

kips_bay_s = get_stats(kips_bay)
kips_bay_s['location'] = 'Kips Bay'
kips_bay_s = reorder(kips_bay_s)

civic_center = new_york[(new_york['neighbourhood_cleansed'] == 'Civic Center')]
civic_center.head()
civic_center.reset_index(inplace=True)
civic_center =  civic_center.drop('index', axis =1)

civic_center_s = get_stats(civic_center)
civic_center_s['location'] = 'Civic Center'
civic_center_s = reorder(civic_center_s)

two_bridges = new_york[(new_york['neighbourhood_cleansed'] == 'Two Bridges')]
two_bridges.head()
two_bridges.reset_index(inplace=True)
two_bridges =  two_bridges.drop('index', axis =1)

two_bridges_s = get_stats(two_bridges)
two_bridges_s['location'] = 'Two Bridges'
two_bridges_s = reorder(two_bridges_s)

#%%
#Queens

long_island = new_york[(new_york['neighbourhood_cleansed'] == 'Long Island City')]
long_island.head()
long_island.reset_index(inplace=True)
long_island =  long_island.drop('index', axis =1)

long_island_s = get_stats(long_island)
long_island_s['location'] = 'Long Island City'
long_island_s = reorder(long_island_s)

ditmars_steinway = new_york[(new_york['neighbourhood_cleansed'] == 'Ditmars Steinway')]
ditmars_steinway.head()
ditmars_steinway.reset_index(inplace=True)
ditmars_steinway =  ditmars_steinway.drop('index', axis =1)

ditmars_steinway_s = get_stats(ditmars_steinway)
ditmars_steinway_s['location'] = 'Ditmars Steinway'
ditmars_steinway_s = reorder(ditmars_steinway_s)

glen_oaks = new_york[(new_york['neighbourhood_cleansed'] == 'Glen Oaks')]
glen_oaks.head()
glen_oaks.reset_index(inplace=True)
glen_oaks =  glen_oaks.drop('index', axis =1)

glen_oaks_s = get_stats(glen_oaks)
glen_oaks_s['location'] = 'Glen Oaks'
glen_oaks_s = reorder(glen_oaks_s)

sunnyside = new_york[(new_york['neighbourhood_cleansed'] == 'Sunnyside')]
sunnyside.head()
sunnyside.reset_index(inplace=True)
sunnyside =  sunnyside.drop('index', axis =1)

sunnyside_s = get_stats(sunnyside)
sunnyside_s['location'] = 'Sunnyside'
sunnyside_s = reorder(sunnyside_s)

astoria = new_york[(new_york['neighbourhood_cleansed'] == 'Astoria')]
astoria.head()
astoria.reset_index(inplace=True)
astoria =  astoria.drop('index', axis =1)

astoria_s = get_stats(astoria)
astoria_s['location'] = 'Astoria'
astoria_s = reorder(astoria_s)

flushing = new_york[(new_york['neighbourhood_cleansed'] == 'Flushing')]
flushing.head()
flushing.reset_index(inplace=True)
flushing =  flushing.drop('index', axis =1)

flushing_s = get_stats(flushing)
flushing_s['location'] = 'Flushing'
flushing_s = reorder(flushing_s)

college_point = new_york[(new_york['neighbourhood_cleansed'] == 'College Point')]
college_point.head()
college_point.reset_index(inplace=True)
college_point =  college_point.drop('index', axis =1)

college_point_s = get_stats(college_point)
college_point_s['location'] = 'College Point'
college_point_s = reorder(college_point_s)

whitestone = new_york[(new_york['neighbourhood_cleansed'] == 'Whitestone')]
whitestone.head()
whitestone.reset_index(inplace=True)
whitestone =  whitestone.drop('index', axis =1)

whitestone_s = get_stats(whitestone)
whitestone_s['location'] = 'Whitestone'
whitestone_s = reorder(whitestone_s)

bayside = new_york[(new_york['neighbourhood_cleansed'] == 'Bayside')]
bayside.head()
bayside.reset_index(inplace=True)
bayside =  bayside.drop('index', axis =1)

bayside_s = get_stats(bayside)
bayside_s['location'] = 'Bayside'
bayside_s = reorder(bayside_s)

little_neck = new_york[(new_york['neighbourhood_cleansed'] == 'Little Neck')]
little_neck.head()
little_neck.reset_index(inplace=True)
little_neck =  little_neck.drop('index', axis =1)

little_neck_s = get_stats(little_neck)
little_neck_s['location'] = 'Little Neck'
little_neck_s = reorder(little_neck_s)

fresh_meadows = new_york[(new_york['neighbourhood_cleansed'] == 'Fresh Meadows')]
fresh_meadows.head()
fresh_meadows.reset_index(inplace=True)
fresh_meadows =  fresh_meadows.drop('index', axis =1)

fresh_meadows_s = get_stats(fresh_meadows)
fresh_meadows_s['location'] = 'Fresh Meadows'
fresh_meadows_s = reorder(fresh_meadows_s)

corona = new_york[(new_york['neighbourhood_cleansed'] == 'Corona')]
corona.head()
corona.reset_index(inplace=True)
corona =  corona.drop('index', axis =1)

corona_s = get_stats(corona)
corona_s['location'] = 'Corona'
corona_s = reorder(corona_s)

east_elmhurst = new_york[(new_york['neighbourhood_cleansed'] == 'East Elmhurst')]
east_elmhurst.head()
east_elmhurst.reset_index(inplace=True)
east_elmhurst =  east_elmhurst.drop('index', axis =1)

east_elmhurst_s = get_stats(east_elmhurst)
east_elmhurst_s['location'] = 'East Elmhurst'
east_elmhurst_s = reorder(east_elmhurst_s)

jackson_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Jackson Heights')]
jackson_heights.head()
jackson_heights.reset_index(inplace=True)
jackson_heights =  jackson_heights.drop('index', axis =1)

jackson_heights_s = get_stats(jackson_heights)
jackson_heights_s['location'] = 'Jackson Heights'
jackson_heights_s = reorder(jackson_heights_s)

forest_hills = new_york[(new_york['neighbourhood_cleansed'] == 'Forest Hills')]
forest_hills.head()
forest_hills.reset_index(inplace=True)
forest_hills =  forest_hills.drop('index', axis =1)

forest_hills_s = get_stats(forest_hills)
forest_hills_s['location'] = 'Forest Hills'
forest_hills_s = reorder(forest_hills_s)

woodside = new_york[(new_york['neighbourhood_cleansed'] == 'Woodside')]
woodside.head()
woodside.reset_index(inplace=True)
woodside =  woodside.drop('index', axis =1)

woodside_s = get_stats(woodside)
woodside_s['location'] = 'Woodside'
woodside_s = reorder(woodside_s)

maspeth = new_york[(new_york['neighbourhood_cleansed'] == 'Maspeth')]
maspeth.head()
maspeth.reset_index(inplace=True)
maspeth =  maspeth.drop('index', axis =1)

maspeth_s = get_stats(maspeth)
maspeth_s['location'] = 'Maspeth'
maspeth_s = reorder(maspeth_s)

middle_village = new_york[(new_york['neighbourhood_cleansed'] == 'Middle Village')]
middle_village.head()
middle_village.reset_index(inplace=True)
middle_village =  middle_village.drop('index', axis =1)

middle_village_s = get_stats(middle_village)
middle_village_s['location'] = 'Middle Village'
middle_village_s = reorder(middle_village_s)

ridgewood = new_york[(new_york['neighbourhood_cleansed'] == 'Ridgewood')]
ridgewood.head()
ridgewood.reset_index(inplace=True)
ridgewood =  ridgewood.drop('index', axis =1)

ridgewood_s = get_stats(ridgewood)
ridgewood_s['location'] = 'Ridgewood'
ridgewood_s = reorder(ridgewood_s)

cambria_heights = new_york[(new_york['neighbourhood_cleansed'] == 'Cambria Heights')]
cambria_heights.head()
cambria_heights.reset_index(inplace=True)
cambria_heights =  cambria_heights.drop('index', axis =1)

cambria_heights_s = get_stats(cambria_heights)
cambria_heights_s['location'] = 'Cambria Heights'
cambria_heights_s = reorder(cambria_heights_s)

springfield = new_york[(new_york['neighbourhood_cleansed'] == 'Springfield Gardens')]
springfield.head()
springfield.reset_index(inplace=True)
springfield =  springfield.drop('index', axis =1)

springfield_s = get_stats(springfield)
springfield_s['location'] = 'Springfield Gardens'
springfield_s = reorder(springfield_s)

howard_beach = new_york[(new_york['neighbourhood_cleansed'] == 'Howard Beach')]
howard_beach.head()
howard_beach.reset_index(inplace=True)
howard_beach =  howard_beach.drop('index', axis =1)

howard_beach_s = get_stats(howard_beach)
howard_beach_s['location'] = 'Howard Beach'
howard_beach_s = reorder(howard_beach_s)

kew_gardens = new_york[(new_york['neighbourhood_cleansed'] == 'Kew Gardens')]
kew_gardens.head()
kew_gardens.reset_index(inplace=True)
kew_gardens =  kew_gardens.drop('index', axis =1)

kew_gardens_s = get_stats(kew_gardens)
kew_gardens_s['location'] = 'Kew Gardens'
kew_gardens_s = reorder(kew_gardens_s)

ozone = new_york[(new_york['neighbourhood_cleansed'] == 'Ozone Park')]
ozone.head()
ozone.reset_index(inplace=True)
ozone =  ozone.drop('index', axis =1)

ozone_s = get_stats(ozone)
ozone_s['location'] = 'Ozone Park'
ozone_s = reorder(ozone_s)

richmond_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Richmond Hill')]
richmond_hill.head()
richmond_hill.reset_index(inplace=True)
richmond_hill =  richmond_hill.drop('index', axis =1)

richmond_hill_s = get_stats(richmond_hill)
richmond_hill_s['location'] = 'Richmond Hill'
richmond_hill_s = reorder(richmond_hill_s)

south_ozone_park = new_york[(new_york['neighbourhood_cleansed'] == 'South Ozone Park')]
south_ozone_park.head()
south_ozone_park.reset_index(inplace=True)
south_ozone_park =  south_ozone_park.drop('index', axis =1)

south_ozone_park_s = get_stats(south_ozone_park)
south_ozone_park_s['location'] = 'South Ozone Park'
south_ozone_park_s = reorder(south_ozone_park_s)

woodhaven = new_york[(new_york['neighbourhood_cleansed'] == 'Woodhaven')]
woodhaven.head()
woodhaven.reset_index(inplace=True)
woodhaven =  woodhaven.drop('index', axis =1)

woodhaven_s = get_stats(woodhaven)
woodhaven_s['location'] = "Woodhaven"
woodhaven_s = reorder(woodhaven_s)

rosedale = new_york[(new_york['neighbourhood_cleansed'] == 'Rosedale')]
rosedale.head()
rosedale.reset_index(inplace=True)
rosedale =  rosedale.drop('index', axis =1)

rosedale_s = get_stats(rosedale)
rosedale_s['location'] = 'Rosedale'
rosedale_s = reorder(rosedale_s)

hollis = new_york[(new_york['neighbourhood_cleansed'] == 'Hollis')]
hollis.head()
hollis.reset_index(inplace=True)
hollis =  hollis.drop('index', axis =1)

hollis_s = get_stats(hollis)
hollis_s['location'] = 'Hollis'
hollis_s = reorder(hollis_s)

bellerose = new_york[(new_york['neighbourhood_cleansed'] == 'Bellerose')]
bellerose.head()
bellerose.reset_index(inplace=True)
bellerose = bellerose.drop('index', axis =1)

bellerose_s = get_stats(bellerose)
bellerose_s['location'] = 'Bellerose'
bellerose_s = reorder(bellerose_s)

queens_village = new_york[(new_york['neighbourhood_cleansed'] == 'Queens Village')]
queens_village.head()
queens_village.reset_index(inplace=True)
queens_village = queens_village.drop('index', axis =1)

queens_village_s = get_stats(queens_village)
queens_village_s['location'] = 'Queens Village'
queens_village_s = reorder(queens_village_s)

jamaica = new_york[(new_york['neighbourhood_cleansed'] == 'Jamaica')]
jamaica.head()
jamaica.reset_index(inplace=True)
jamaica = jamaica.drop('index', axis =1)

jamaica_s = get_stats(jamaica)
jamaica_s['location'] = 'Jamaica'
jamaica_s = reorder(jamaica_s)

edgemere = new_york[(new_york['neighbourhood_cleansed'] == 'Edgemere')]
edgemere.head()
edgemere.reset_index(inplace=True)
edgemere = edgemere.drop('index', axis =1)

edgemere_s = get_stats(edgemere)
edgemere_s['location'] = 'Edgemere'
edgemere_s = reorder(edgemere_s)

elmhurst = new_york[(new_york['neighbourhood_cleansed'] == 'Elmhurst')]
elmhurst.head()
elmhurst.reset_index(inplace=True)
elmhurst = elmhurst.drop('index', axis =1)

elmhurst_s = get_stats(elmhurst)
elmhurst_s['location'] = 'Elmhurst'
elmhurst_s = reorder(elmhurst_s)

rego_park = new_york[(new_york['neighbourhood_cleansed'] == 'Rego Park')]
rego_park.head()
rego_park.reset_index(inplace=True)
rego_park = rego_park.drop('index', axis =1)

rego_park_s = get_stats(rego_park)
rego_park_s['location'] = 'Rego Park'
rego_park_s = reorder(rego_park_s)

glendale = new_york[(new_york['neighbourhood_cleansed'] == 'Glendale')]
glendale.head()
glendale.reset_index(inplace=True)
glendale = glendale.drop('index', axis =1)

glendale_s = get_stats(glendale)
glendale_s['location'] = 'Glendale'
glendale_s = reorder(glendale_s)

#%%
#Staten Island

silver_lake = new_york[(new_york['neighbourhood_cleansed'] == 'Silver Lake')]
silver_lake.head()
silver_lake.reset_index(inplace=True)
silver_lake = silver_lake.drop('index', axis =1)

silver_lake_s = get_stats(silver_lake)
silver_lake_s['location'] = 'Silver Lake'
silver_lake_s = reorder(silver_lake_s)

west_brighton = new_york[(new_york['neighbourhood_cleansed'] == 'West Brighton')]
west_brighton.head()
west_brighton.reset_index(inplace=True)
west_brighton = west_brighton.drop('index', axis =1)

west_brighton_s = get_stats(west_brighton)
west_brighton_s['location'] = 'West Brighton'
west_brighton_s = reorder(west_brighton_s)

grymes_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Grymes Hill')]
grymes_hill.head()
grymes_hill.reset_index(inplace=True)
grymes_hill = grymes_hill.drop('index', axis =1)

grymes_hill_s = get_stats(grymes_hill)
grymes_hill_s['location'] = 'Grymes Hill'
grymes_hill_s = reorder(grymes_hill_s)

great_kills = new_york[(new_york['neighbourhood_cleansed'] == 'Great Kills')]
great_kills.head()
great_kills.reset_index(inplace=True)
great_kills = great_kills.drop('index', axis =1)

great_kills_s = get_stats(great_kills)
great_kills_s['location'] = 'Great Kills'
great_kills_s = reorder(great_kills_s)

rosebank = new_york[(new_york['neighbourhood_cleansed'] == 'Rosebank')]
rosebank.head()
rosebank.reset_index(inplace=True)
rosebank = rosebank.drop('index', axis =1)

rosebank_s = get_stats(rosebank)
rosebank_s['location'] = 'Rosebank'
rosebank_s = reorder(rosebank_s)

tottenville = new_york[(new_york['neighbourhood_cleansed'] == 'Tottenville')]
tottenville.head()
tottenville.reset_index(inplace=True)
tottenville = tottenville.drop('index', axis =1)

tottenville_s = get_stats(tottenville)
tottenville_s['location'] = 'Tottenville'
tottenville_s = reorder(tottenville_s)

rossville = new_york[(new_york['neighbourhood_cleansed'] == 'Rossville')]
rossville.head()
rossville.reset_index(inplace=True)
rossville = rossville.drop('index', axis =1)

rossville_s = get_stats(rossville)
rossville_s['location'] = 'Rossville'
rossville_s = reorder(rossville_s)

west_brighton = new_york[(new_york['neighbourhood_cleansed'] == 'West Brighton')]
west_brighton.head()
west_brighton.reset_index(inplace=True)
west_brighton = west_brighton.drop('index', axis =1)

west_brighton_s = get_stats(west_brighton)
west_brighton_s['location'] = 'West Brighton'
west_brighton_s = reorder(west_brighton_s)

bull_head = new_york[(new_york['neighbourhood_cleansed'] == 'Bull\'s Head')]
bull_head.head()
bull_head.reset_index(inplace=True)
bull_head = bull_head.drop('index', axis =1)

bull_head_s = get_stats(bull_head)
bull_head_s['location'] = 'Bull\'s Head'
bull_head_s = reorder(bull_head_s)

emerson_hill = new_york[(new_york['neighbourhood_cleansed'] == 'Emerson Hill')]   
emerson_hill.head()
emerson_hill.reset_index(inplace=True)
emerson_hill = emerson_hill.drop('index', axis=1)

emerson_hill_s = get_stats(emerson_hill)
emerson_hill_s['location'] = 'Emerson Hill'
emerson_hill_s = reorder(emerson_hill_s)

randall_manor = new_york[(new_york['neighbourhood_cleansed'] == 'Randall Manor')]   
randall_manor.head()
randall_manor.reset_index(inplace=True)
randall_manor = randall_manor.drop('index', axis =1)

randall_manor_s = get_stats(randall_manor)
randall_manor_s['location'] = 'Randall Manor'
randall_manor_s = reorder(randall_manor_s)

#%%

statistics = concat([east_flatbush_s, bensonhurst_s, williamsburg_s, city_island_s, bay_ridge_s, mariners_harbor_s, crown_heights_s, south_ozone_park_s, bedford_stuyvesant_s,
                    boerum_hill_s, kensington_s, borough_park_s, bushwick_s, greenpoint_s, coney_island_s, flatbush_s, dyker_heights_s, sheepshead_bay_s, red_hook_s, bergen_beach_s,
                    canarsie_s, prospect_heights_s, east_flatbush_s, carroll_gardens_s, fort_greene_s, prospect_lefferts_s, brighton_beach_s, dumbo_s, columbia_s, cypress_hills_s, park_slope_s,
                    gravesend_s, sunset_park_s, sunset_park_s, cobble_hill_s, gowanus_s, downtown_brooklyn_s, bath_beach_s, chelsea_s, lower_east_side_s, east_village_s, fidi_s, flatiron_s,
                    noho_s, soho_s, tribeca_s, west_village_s, murray_hill_s, upper_east_s, upper_west_s, midtown_s, harlem_s, east_harlem_s, washington_heights_s, theater_district_s, 
                    hells_kitchen_s, clinton_hill_s, roosevelt_island_s, battery_park_s, riverdale_s, long_island_s, ditmars_steinway_s, inwood_s, gramercy_s, nolita_s, chinatown_s, 
                    kips_bay_s, civic_center_s, two_bridges_s, glen_oaks_s, sunnyside_s, astoria_s, flushing_s, college_point_s, whitestone_s, bayside_s, little_neck_s, fresh_meadows_s, 
                    corona_s, east_elmhurst_s, jackson_heights_s, forest_hills_s, woodside_s, maspeth_s, middle_village_s, ridgewood_s, cambria_heights_s, springfield_s, howard_beach_s, 
                    kew_gardens_s, ozone_s, richmond_hill_s, south_ozone_park_s, woodhaven_s, rosedale_s, hollis_s, bellerose_s, queens_village_s, jamaica_s, edgemere_s, elmhurst_s, 
                    rego_park_s, glendale_s, south_ozone_park_s, silver_lake_s, west_brighton_s, grymes_hill_s, rosebank_s, great_kills_s, tottenville_s, rossville_s, west_brighton_s,
                    bull_head_s, emerson_hill_s, randall_manor_s, longwood_s, clifton_s, charleston_s, st_george_s, windsor_terrace_s, pelham_gardens_s, kingsbridge_s, fieldston_s])
                    

statistics.count()

statistics.columns.values

#%%

bronx = {'Pelham Bey': len(pelham_bay), 'Morris Park' : len(morris_park), 'Bronxdale' : len(bronxdale), 'Eastchester' : len(eastchester),
     'Wakefield': len(wakefield), 'Kingsbridge' : len(kingsbridge), 'Pelham Gardens': len(pelham_gardens), 'Fieldston' : len(fieldston),
     'Soundview': len(soundview), 'Mount Eden' : len(mount_eden), 'Port Morris': len(port_morris), 'Allerton' : len(allerton),
     'Belmont': len(belmont), 'St. Albans' : len(st_albans), 'East Morrisania': len(east_morrisania), 'University Heights' : len(university_heights),
     'Van Nest': len(van_nest), 'Morris Heights' : len(morris_heights), 'Claremont Village': len(claremont_village), }

bronx_df = DataFrame(bronx, index=[0]).stack()
bronx_df = DataFrame(bronx_df).sort_values([0], ascending=[False]).reset_index(0)
bronx_df = bronx_df[0]
bronx_df = DataFrame(bronx_df)
bronx_df.columns = ['Count of Listings']
bronx_df

bronx_df['Count of Listings'].plot(kind = 'bar', cmap = cmap)
plt.title('Count of Listings')

#brooklyn = {'East Flatbush': len(east_flatbush), 'Bensonhurst' : len(bensonhurst), 'Williamsburg' : len(williamsburg), 'City Island' : len(city_island),
#     'Bay Ridge': len(bay_ridge), 'Marine Harbor' : len(mariners_harbor), 'Crown Heights': len(crown_heights), 'South Slope' : len(south_slope),
#     'Bedford-Stuyvesant': len(bedford_stuyvesant), 'Boerum Hill' : len(boerum_hill), 'Kensington': len(kensington), 'Borough Park' : len(borough_park),
#     'Bushwich': len(bushwick), 'Greenpoint' : len(greenpoint), 'Coney Island': len(coney_island), 'Flatbush' : len(flatbush),
#     'Dyker Heights': len(dyker_heights), 'Sheepshead Bay' : len(sheepshead_bay), 'Red Hook': len(red_hook), 'Bergen Beach': len(bergen_beach),
#     'Canarsie': len(canarsie), 'Prospect Heights' : len(prospect_heights), 'East Flatbush': len(east_flatbush), 'Carroll Gardens': len(carroll_gardens),
#     'Fort Greene': len(fort_greene), 'Prospect-Lefferts Gardens' : len(prospect_lefferts), 'Brighton Beach': len(brighton_beach), 'DUMBO': len(dumbo),
#     'Columbia St': len(columbia), 'Cypress Hills' : len(cypress_hills), 'Gravesend': len(gravesend), 'Sunset Park': len(sunset_park),
#     'Cobble Hill': len(cobble_hill), 'Gowanus' : len(gowanus), 'Downtown Brooklyn': len(downtown_brooklyn), 'Bath Beach': len(bath_beach)}

#brooklyn_df = DataFrame(brooklyn, index=[0]).stack()
#brooklyn_df = DataFrame(brooklyn_df).sort_values([0], ascending=[False]).reset_index(0)
#brooklyn_df = brooklyn_df[0]
#brooklyn_df = DataFrame(brooklyn_df)
#brooklyn_df.columns = ['Count of Listings']
#brooklyn_df

#brooklyn_df['Count of Listings'].plot(kind = 'bar', cmap = cmap)
#plt.title('Count of Listings')

#mahattan = {'Chelsea': len(chelsea), 'Lower East Side' : len(lower_east_side), 'Financial District' : len(fidi), 'East Village' : len(east_village),
#     'Flatiron District': len(flatiron), 'NoHo' : len(noho), 'SoHo': len(soho), 'Tribeca' : len(tribeca),
#     'West Village': len(west_village), 'Murray Hill' : len(murray_hill), 'Upper West Side': len(upper_west), 'Upper East Side' : len(upper_east),
#     'Midtown': len(midtown), 'Harlem' : len(harlem), 'East Harlem': len(east_harlem), 'Washington Heights' : len(washington_heights),
#     'Theater District': len(theater_district), f"Hell's Kitchen" : len(hells_kitchen), 'Clinton Hill': len(clinton_hill), 'Roosevelt Island': len(roosevelt_island),
#     'Battery Park City': len(battery_park), 'Riverdale' : len(riverdale), 'Long Island City': len(long_island), 'Ditmars Steinway': len(ditmars_steinway),
#     'Inwood': len(inwood), 'Gramercy' : len(gramercy), 'Nolita': len(nolita), 'Chinatown': len(chinatown),
#     'Kips Bay': len(kips_bay), 'Civic Center' : len(civic_center), 'Two Bridges': len(two_bridges)}

#mahattan_df = DataFrame(mahattan, index=[0]).stack()
#mahattan_df = DataFrame(mahattan_df).sort_values([0], ascending=[False]).reset_index(0)
#mahattan_df = mahattan_df[0]
#mahattan_df = DataFrame(mahattan_df)
#mahattan_df.columns = ['Count of Listings']
#mahattan_df

#mahattan_df['Count of Listings'].plot(kind = 'bar', cmap = cmap)
#plt.title('Count of Listings')

#queens = {'Glen Oaks': len(glen_oaks), 'Sunnyside' : len(sunnyside), 'Astoria' : len(astoria), 'Flushing' : len(flushing),
#     'College Point': len(college_point), 'Whitestone' : len(whitestone), 'Bayside': len(bayside), 'Little Neck' : len(little_neck),
#     'Fresh Meadows': len(fresh_meadows), 'Corona' : len(corona), 'East Elmhurst': len(east_elmhurst), 'Jackson Heights' : len(jackson_heights),
#     'Forst Hills': len(forest_hills), 'Woodside' : len(woodside), 'Maspeth': len(maspeth), 'Middle Village' : len(ridgewood),
#     'Cambria Heights': len(cambria_heights), 'Springfield Gardens' : len(springfield), 'Howard Beach': len(howard_beach), 'Roosevelt Island': len(roosevelt_island),
#     'Kew Gardnes': len(kew_gardens), 'Ozone Park' : len(ozone), 'Richmond Hill': len(richmond_hill), 'South Ozone Park': len(south_ozone_park),
#     'Woodhaven': len(woodhaven), 'Rosedale' : len(rosedale), 'Hollis': len(hollis), 'Bellerose': len(bellerose),
#     'Queens Village': len(queens_village), 'Jamaica' : len(jamaica), 'Edgemere': len(edgemere), 'Elmhurst': len(elmhurst),
#     'Rego Park': len(rego_park), 'Glendale' : len(glendale)}

#queens_df = DataFrame(queens, index=[0]).stack()
#queens_df = DataFrame(queens_df).sort_values([0], ascending=[False]).reset_index(0)
#queens_df = queens_df[0]
#queens_df = DataFrame(queens_df)
#queens_df.columns = ['Count of Listings']
#queens_df

#queens_df['Count of Listings'].plot(kind = 'bar', cmap = cmap)
#plt.title('Count of Listings')

#staten_island = {'Silver Lake': len(silver_lake), 'West Brighton' : len(west_brighton), 'Gyrmes Hill' : len(grymes_hill), 'Rosebank' : len(rosebank),
#     'Great Kills': len(great_kills), 'Tottenville' : len(tottenville), 'Rossville': len(rossville), 'West Brighton' : len(west_brighton),
#     f"Bull's Head": len(bull_head), 'Emerson Hill' : len(emerson_hill), 'Randall Manor': len(randall_manor), 'Longwood' : len(long_island),
#     'Clifton': len(clifton), 'Charleston' : len(charleston), 'St. George': len(st_george), 'Windsor Terrace' : len(windsor_terrace)}

#staten_island_df = DataFrame(staten_island, index=[0]).stack()
#staten_island_df = DataFrame(staten_island_df).sort_values([0], ascending=[False]).reset_index(0)
#staten_island_df = staten_island_df[0]
#staten_island_df = DataFrame(staten_island_df)
#staten_island_df.columns = ['Count of Listings']
#staten_island_df

#staten_island_df['Count of Listings'].plot(kind = 'bar', cmap = cmap)
#plt.title('Count of Listings')

#x = {'Pelham Bay': len(pelham_bay), 'Morris Park' : len(morris_park), 'Bronxdale' : len(bronxdale), 'Eastchester' : len(eastchester), 
#     'Wakefield': len(wakefield), 'Kingsbridge' : len(kingsbridge), 'Pelham Gardens': len(pelham_gardens), 'Fieldston' : len(fieldston),
#     'Soundview': len(soundview), 'Mount Eden' : len(mount_eden), 'Port Morris': len(port_morris), 'Allerton' : len(allerton),
#     'Belmont': len(belmont), 'St. Albans' : len(st_albans), 'East Morrisania': len(east_morrisania), 'University Heights' : len(university_heights),
#     'Van Nest': len(van_nest), 'Morris Heights' : len(morris_heights), 'Claremont Village': len(claremont_village), 'East Flatbush': len(east_flatbush),
#     'Bensonhurst' : len(bensonhurst), 'Williamsburg' : len(williamsburg), 'City Island' : len(city_island), 'Bay Ridge': len(bay_ridge), 
#     'Marine Harbor' : len(mariners_harbor), 'Crown Heights': len(crown_heights), 'South Slope' : len(south_slope), 'Bedford-Stuyvesant': len(bedford_stuyvesant), 
#     'Boerum Hill' : len(boerum_hill), 'Kensington': len(kensington), 'Borough Park' : len(borough_park), 'Bushwich': len(bushwick), 'Greenpoint' : len(greenpoint),
#     'Coney Island': len(coney_island), 'Flatbush' : len(flatbush), 'Dyker Heights': len(dyker_heights), 'Sheepshead Bay' : len(sheepshead_bay), 'Red Hook': len(red_hook), 
#     'Bergen Beach': len(bergen_beach),'Canarsie': len(canarsie), 'Prospect Heights' : len(prospect_heights), 'East Flatbush': len(east_flatbush), 
#     'Carroll Gardens': len(carroll_gardens),'Fort Greene': len(fort_greene), 'Prospect-Lefferts Gardens' : len(prospect_lefferts), 'Brighton Beach': len(brighton_beach), 
#     'DUMBO': len(dumbo),'Columbia St': len(columbia), 'Cypress Hills' : len(cypress_hills), 'Gravesend': len(gravesend), 'Sunset Park': len(sunset_park),
#     'Cobble Hill': len(cobble_hill), 'Gowanus' : len(gowanus), 'Downtown Brooklyn': len(downtown_brooklyn), 'Bath Beach': len(bath_beach), 
#     'Chelsea': len(chelsea), 'Lower East Side' : len(lower_east_side), 'Financial District' : len(fidi), 'East Village' : len(east_village),
#     'Flatiron District': len(flatiron), 'NoHo' : len(noho), 'SoHo': len(soho), 'Tribeca' : len(tribeca), 'West Village': len(west_village), 
#     'Murray Hill' : len(murray_hill), 'Upper West Side': len(upper_west), 'Upper East Side' : len(upper_east), 'Midtown': len(midtown), 
#     'Harlem' : len(harlem), 'East Harlem': len(east_harlem), 'Washington Heights' : len(washington_heights),'Theater District': len(theater_district), 
#     f"Hell's Kitchen" : len(hells_kitchen), 'Clinton Hill': len(clinton_hill), 'Roosevelt Island': len(roosevelt_island), 'Battery Park City': len(battery_park), 
#     'Riverdale' : len(riverdale), 'Long Island City': len(long_island), 'Ditmars Steinway': len(ditmars_steinway),'Inwood': len(inwood), 'Gramercy' : len(gramercy), 
#     'Nolita': len(nolita), 'Chinatown': len(chinatown), 'Kips Bay': len(kips_bay), 'Civic Center' : len(civic_center), 'Two Bridges': len(two_bridges),
#     'Glen Oaks': len(glen_oaks), 'Sunnyside' : len(sunnyside), 'Astoria' : len(astoria), 'Flushing' : len(flushing),
#     'College Point': len(college_point), 'Whitestone' : len(whitestone), 'Bayside': len(bayside), 'Little Neck' : len(little_neck),
#    'Fresh Meadows': len(fresh_meadows), 'Corona' : len(corona), 'East Elmhurst': len(east_elmhurst), 'Jackson Heights' : len(jackson_heights),
#     'Forest Hills': len(forest_hills), 'Woodside' : len(woodside), 'Maspeth': len(maspeth), 'Middle Village' : len(ridgewood),
#     'Cambria Heights': len(cambria_heights), 'Springfield Gardens' : len(springfield), 'Howard Beach': len(howard_beach), 'Roosevelt Island': len(roosevelt_island),
#     'Kew Gardnes': len(kew_gardens), 'Ozone Park' : len(ozone), 'Richmond Hill': len(richmond_hill), 'South Ozone Park': len(south_ozone_park),
#     'Woodhaven': len(woodhaven), 'Rosedale' : len(rosedale), 'Hollis': len(hollis), 'Bellerose': len(bellerose),'Queens Village': len(queens_village), 
#    'Jamaica' : len(jamaica), 'Edgemere': len(edgemere), 'Elmhurst': len(elmhurst),'Rego Park': len(rego_park), 'Glendale' : len(glendale),
#     'Silver Lake': len(silver_lake), 'West Brighton' : len(west_brighton), 'Gyrmes Hill' : len(grymes_hill), 'Rosebank' : len(rosebank),
#     'Great Kills': len(great_kills), 'Tottenville' : len(tottenville), 'Rossville': len(rossville), 'West Brighton' : len(west_brighton),
#     f"Bull's Head": len(bull_head), 'Emerson Hill' : len(emerson_hill), 'Randall Manor': len(randall_manor), 'Longwood' : len(long_island),
#     'Clifton': len(clifton), 'Charleston' : len(charleston), 'St. George': len(st_george), 'Windsor Terrace' : len(windsor_terrace)}



df = DataFrame(x, index=[0]).stack()
df = DataFrame(df).sort_values([0], ascending=[False]).reset_index(0)
df = df[0]
df = DataFrame(df)
df.columns = ['Count of Listings']
df

#Normalizing for Population
#%%

pop = read_csv('DataScience\pop_cities_census.csv').convert_objects(convert_numeric=True)
pop.columns = ['City', 'Population']
pop
pop = pop.set_index('City')

#Merging with listing data and normalizing
df1 = concat([df, pop], axis= 1)
df1 = df1.astype('float')
df1['Normalized by Population'] = df1['Count of Listings'] / df1['Population']
df1.sort_values(['Normalized by Population'], ascending=[False]).reset_index(0)
df1


#Estimating Supply and Demand of Listings: Popularity and Normalized Count of Listings
#%%



z = [(365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True), df1['Normalized by Population']]
z.sort

df1 = concat(z, axis = 1)

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
df3 = concat(z, axis = 1)

x = df3['Normalized by Population']
y = df3['mean']

n = (df3.index.tolist())

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

x = ['Williamsburg', 'Bedford-Stuyvesant', 'Harlem', 'Bushwich', 'Upper West Side', f"Hell's Kitchen", 'East Village',
    'Upper East Side', 'Midtown', 'Crown Heights', 'Chelsea', 'Greenpoint', 'East Harlem', 'Astoria', 'Lower East Side',
    'Washington Heights', 'West Village', 'Financial District', 'Flatbush', 'Clinton Hill', 'Murray Hill', 'Prospect-Lefferts Gardens',
    'Longwood', 'Long Island City', 'East Flatbush', 'Kips Bay', 'Fort Greene', 'Middle Village', 'Flushing', 'Sunset Park',
    'SoHo', 'Gramercy', 'Chinatown', 'Prospect Heights', 'Sunnyside', 'Ditmars Steinway', 'Nolita', 'South Slope', 'Theater District',
    'Gowanus', 'Inwood', 'Elmhurst', 'Carroll Gardens', 'Jamaica', 'Woodside', 'Kensington', 'Jackson Heights', 'East Elmhurst',
    'Boerum Hill', 'Tribeca', 'Windsor Terrace', 'Sheepshead Bay', 'Canarsie', 'Borough Park', 'Bay Ridge', 'Forest Hills',
    'Cypress Hills', 'Flatiron District', 'Cobble Hill', 'Rego Park', 'Maspeth', 'Richmond Hill', 'Roosevelt Island', 'Woodhaven',
    'Bensonhurst', 'Springfield Gardens', 'Downtown Brooklyn', 'St. Albans', 'Red Hook', 'NoHo', 'Two Bridges', 'Gravesend', 'Battery Park City',
    'Brighton Beach', 'Corona', 'Ozone Park', 'Kingsbridge', 'Queens Village', 'Rosedale', 'Glendale', 'Port Morris', 'Civic Center', 'St. George',
    'Kew Gardnes', 'South Ozone Park', 'Columbia St', 'Wakefield', 'Bayside', 'Allerton', 'DUMBO', 'Fresh Meadows', 'Pelham Gardens',
    'Belmont', 'Bronxdale', 'Cambria Heights', 'Morris Heights', 'University Heights', 'College Point', 'Claremont Village', 'Randall Manor',
    'Dyker Heights', 'City Island', 'Howard Beach', 'Clifton', 'Bath Beach', 'West Brighton', 'Whitestone', 'Coney Island', 'Morris Park',
    'Pelham Bay', 'Soundview', 'Hollis', 'Fieldston', 'Eastchester', 'Bergen Beach', 'Edgemere', 'East Morrisania', 'Riverdale',
    'Van Nest', 'Great Kills', 'Marine Harbor', 'Bellerose', 'Mount Eden', 'Gyrmes Hill', 'Emerson Hill', 'Tottenville', 'Rosebank',
    'Little Neck', f"Bull's Head", 'Glen Oaks', 'Silver Lake', 'Rossville', 'Charleston'] 

y = ['Zhvi', 'MoM', 'QoQ', 'YoY', '5Year', '10Year']

ZHVI = ZHVI.loc[x,y]

#Putting all the data into one Dataframe for correlation analysis

df_zillow = ZHVI
df_zillow.columns = ['ZHVI', 'ZHVI_MoM', 'ZHVI_QoQ', 'ZHVI_YoY', 'ZHVI_5Year', 'ZHVI_10Year']
df_zillow


# How does the median home price of a city influence the price of an Airbnb listing?

df = concat([statistics['price']['mean'], df_zillow['ZHVI']]).dropna()

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
