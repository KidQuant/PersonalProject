import numpy as np
import pandas as pd

welcomeback = pd.read_csv('welcome_back_9_2018.csv')

welcomeback.head()

welcomeback = welcomeback.rename(index= str, columns = {'Email Address':'Email','Member Rating':'Rating'})

for index, row in welcomeback.iterrows():
    if (row['First Name'] == 'Andre' and row['Last Name'] == 'Sealy'):
        welcomeback.drop(index, inplace = True)
    elif (row['First Name'] == 'Nicholas' and row['Last Name'] == 'Gilchrist'):
        welcomeback.drop(index, inplace = True)
    elif (row['First Name'] == 'Joey' and row['Last Name'] == 'Wong'):
        welcomeback.drop(index, inplace = True)
    elif (row['First Name'] == 'Jeffrey' and row['Last Name'] == 'Leder'):
        welcomeback.drop(index, inplace = True)
    elif (row['First Name'] == 'Ephraim' and row['Last Name'] == 'Agbenor'):
        welcomeback.drop(index, inplace = True)

welcomeback[welcomeback['Rating'] >= 3].count().Email
