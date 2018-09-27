import numpy as np
import pandas as pd

fifa_wc_venues = pd.DataFrame({'year':[1998,2002,2006,2010,2014],
                               'host':['France', 'South Korea', 'Germany', 'South Africa', 'Brazil'],
                               'continent':['Europe', 'Asia', 'Europe', 'Africa', 'South America'],
                               'winner':['France','Brazil','Italy','Spain','Germany']})

print(fifa_wc_venues.loc[:,['year', 'winner']])

ratio_to_earth = {
    'mercury':{'gravity':0.378},
    'mars':{'gravity':0.377}}

print(ratio_to_earth)

q = [2.38, 9.67, 9.22, 10.79]

for j, y in enumerate(q):
    print('Element ' + str(j) + ' -', str(y))

x = np.array([[4,5,6],
              [14,15,16]])

np.transpose(x)

def count_digits(y):
    print(len(str(y)))

from functools import reduce
product = [10,1,4]
result = reduce(lambda x, y: x * y, product)
print(result)

def rectangle(length, width):
    a = length * width
    p = 2 * (length + width)
    return a, p

area, perimeter = rectangle(15,3)

print((area, perimeter))

z = 4

def cube(x):
    z = x ** 3
    return z

print(z)
