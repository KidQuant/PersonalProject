import numpy as np

# r1.3

x = list(range(1,20))

def minmax(data):
    min = x[0]
    max = x[-1]
    return min, max

minmax(x)