from heapq import merge
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
from functools import reduce
import pickle

engine = create_engine("mysql+mysqldb://root:root@localhost/Warzone")
my_conn = engine.connect()
gamertagQuery = "SELECT * FROM gamertags"
gamertags = pd.read_sql(gamertagQuery, my_conn)

gamertags[:25]

dfList = []

for i in gamertags['User']:


    query = "SELECT * FROM {}".format(i)
    df = pd.read_sql(query, my_conn)
    dfList.append(df)

mergedDF = reduce(lambda l, r: pd.merge(l, r, on = ['MatchID', 'Mode', 'Kills', 'Deaths', 'KDRatio', 'LobbyKD', 'Date', 'Time', 'User'], how = 'outer'), dfList)

mergedDF['Mode'].unique()

modefilteredDF = mergedDF[~mergedDF['Mode'].str.contains('rebirth') \
    & ~mergedDF['Mode'].str.contains('gld_pldr') \
    & ~mergedDF['Mode'].str.contains('rbrth') \
    & ~mergedDF['Mode'].str.contains('clash') \
    & ~mergedDF['Mode'].str.contains('respect') \
    & ~mergedDF['Mode'].str.contains('olaride') \
    & ~mergedDF['Mode'].str.contains('rxp') \
    & ~mergedDF['Mode'].str.contains('dmz')]


modefilteredDF['Mode'].unique()
len(modefilteredDF)

########################################
# Huskers
########################################

# Removing Breadman
huskerrs = modefilteredDF[modefilteredDF['User'] == 'Huskerrs']
bbreadman = modefilteredDF[modefilteredDF['User'] == 'BBREADMAN']

mergedBbreadman = huskerrs.merge(bbreadman, on = ['MatchID'], how='inner')
filterList = list(mergedBbreadman['MatchID'])
len(filterList)

# Removing fifakill
fifakill = modefilteredDF[modefilteredDF['User'] == 'FifaKill']
mergedfifakill = huskerrs.merge(fifakill, on = ['MatchID'], how='inner')
secondlist = list(mergedfifakill['MatchID'])

for i in secondlist:
    if i not in filterList:
        filterList.append(i)

len(filterList)


huskerrs = huskerrs[~huskerrs.MatchID.isin(filterList)]
len(huskerrs)


with open('data\huskerrs.pickle', 'wb') as f:
    pickle.dump(huskerrs, f)

########################################
# Symfuhny
########################################

# Removing teepee
symfuhny = modefilteredDF[modefilteredDF['User'] == 'Symfuhny']
teepee = modefilteredDF[modefilteredDF['User'] == 'TeePee']

mergedteepee = symfuhny.merge(teepee, on = ['MatchID'], how='inner')
filterList = list(mergedteepee['MatchID'])
len(filterList)

# Removing fifakill
fifakill = modefilteredDF[modefilteredDF['User'] == 'FifaKill']
mergedfifakill = symfuhny.merge(fifakill, on = ['MatchID'], how='inner')
secondlist = list(mergedfifakill['MatchID'])

for i in secondlist:
    if i not in filterList:
        filterList.append(i)

len(filterList)

symfuhny = symfuhny[~symfuhny.MatchID.isin(filterList)]
len(symfuhny)


with open('data\symfuhny.pickle', 'wb') as f:
    pickle.dump(huskerrs, f)

########################################
# Aydan
########################################

# Removing fifakill
aydan = modefilteredDF[modefilteredDF['User'] == 'Aydan']
fifakill = modefilteredDF[modefilteredDF['User'] == 'fifakill']

mergedfifakill = aydan.merge(fifakill, on = ['MatchID'], how='inner')

len(mergedfifakill) / len(aydan)
filterList = list(mergedfifakill['MatchID'])

aydan = aydan[~aydan.MatchID.isin(filterList)]
len(aydan)


with open('data//aydan.pickle', 'wb') as f:
    pickle.dump(aydan, f)

########################################
# Zlaner
########################################

# removing clutchbelk
zlaner = modefilteredDF[modefilteredDF['User'] == 'Zlaner']
clutchbelk = modefilteredDF[modefilteredDF['User'] == 'ClutchBelk']

mergedclutchbelk = zlaner.merge(clutchbelk, on = ['MatchID'], how='inner')

filterList = list(mergedclutchbelk['MatchID'])

zlaner = zlaner[~zlaner.MatchID.isin(filterList)]

with open('data//zlaner.pickle', 'wb') as f:
    pickle.dump(zlaner, f)

########################################
# Teepee
########################################

teepee = modefilteredDF[modefilteredDF['User'] == 'TeePee']
symfuhny = modefilteredDF[modefilteredDF['User'] == 'Symfuhny']
mergedsymfuhny = teepee.merge(symfuhny, on = ['MatchID'], how='inner')

filterList = list(mergedsymfuhny['MatchID'])

teepee = teepee[~teepee.MatchID.isin(filterList)]

with open('data//teepee.pickle', 'wb') as f:
    pickle.dump(teepee, f)

########################################
# BBreadman
########################################

# Removing Bbreadman
bbreadman = modefilteredDF[modefilteredDF['User'] == 'BBREADMAN']
huskerrs = modefilteredDF[modefilteredDF['User'] == 'Huskerrs']

mergedhuskerrs = bbreadman.merge(huskerrs, on = ['MatchID'], how = 'inner')

filterList = list(mergedhuskerrs['MatchID'])

# Removing Fifakill
fifakill = modefilteredDF[modefilteredDF['User'] == 'FifaKill']
mergedfifakill = bbreadman.merge(fifakill, on = ['MatchID'], how = 'inner')

secondlist = list(mergedfifakill['MatchID'])

for i in secondlist:
    if i not in filterList:
        filterList.append(i)

# Removing JoeWo
joewo = modefilteredDF[modefilteredDF['User'] == 'JoeWo']
mergedjoewo = bbreadman.merge(joewo, on = ['MatchID'], how = 'inner')

thirdlist = list(mergedjoewo['MatchID'])

for i in thirdlist:
    if i not in filterList:
        filterList.append(i)

bbreadman = bbreadman[~bbreadman.MatchID.isin(filterList)]

########################################
# SuperEvan
########################################

# Removing Biffle
superevan = modefilteredDF[modefilteredDF['User'] == 'SuperEvan']
biffle = modefilteredDF[modefilteredDF['User'] == 'Biffle']

mergedbiffle = superevan.merge(biffle, on = ['MatchID'], how = 'inner')

filterList = list(mergedbiffle['MatchID'])

superevan = superevan[~superevan.MatchID.isin(filterList)]