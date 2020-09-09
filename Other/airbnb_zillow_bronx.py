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
fieldston_s['location'] = 'Fieldston'
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

statistics = concat([pelham_bay_s, morris_park_s, bronxdale_s, eastchester_s, wakefield_s, kingsbridge_s, pelham_gardens_s, fieldston_s, soundview_s,
                    mount_eden_s, port_morris_s, allerton_s, belmont_s, st_albans_s, east_morrisania_s, university_heights_s, van_nest_s, claremont_village_s,
                    morris_heights_s, longwood_s])


#%%

bronx = {'Pelham Bay': len(pelham_bay), 'Morris Park' : len(morris_park), 'Bronxdale' : len(bronxdale), 'Eastchester' : len(eastchester),
     'Wakefield': len(wakefield), 'Kingsbridge' : len(kingsbridge), 'Pelham Gardens': len(pelham_gardens), 'Fieldston' : len(fieldston),
     'Soundview': len(soundview), 'Mount Eden' : len(mount_eden), 'Port Morris': len(port_morris), 'Allerton' : len(allerton),
     'Belmont': len(belmont), 'St. Albans' : len(st_albans), 'East Morrisania': len(east_morrisania), 'University Heights' : len(university_heights),
     'Van Nest': len(van_nest), 'Morris Heights' : len(morris_heights), 'Claremont Village': len(claremont_village), 'Longwood' : len(longwood) }

bronx_df = DataFrame(bronx, index=[0]).stack()
bronx_df = DataFrame(bronx_df).sort_values([0], ascending=[False]).reset_index(0)
bronx_df = bronx_df[0]
bronx_df = DataFrame(bronx_df)
bronx_df.columns = ['Count of Listings']
bronx_df

bronx_df['Count of Listings'].plot(kind = 'bar', cmap = cmap)
plt.title('Count of Listings')

#Normalizing for Population
#%%

pop = read_csv('DataScience\pop_cities_census_bronx.csv').convert_objects(convert_numeric=True)
pop.columns = ['City', 'Population']
pop
pop = pop.set_index('City')

#Merging with listing data and normalizing
df1 = concat([bronx_df, pop], axis= 1)
df1 = df1.astype('float')
df1['Normalized by Population'] = df1['Count of Listings'] / df1['Population']
df1.sort_values(['Normalized by Population'], ascending=[False]).reset_index(0)
df1

z = [(365 - statistics['availability_365']['mean']).convert_objects(convert_numeric=True), df1['Normalized by Population']]
df2 = concat(z, axis = 1)
df2

