import pandas as pd
import numpy as np
from scipy.stats import rankdata
from sklearn.model_selection import cross_val_predict

train['is_test'] = 0
test['is_test'] = 1
