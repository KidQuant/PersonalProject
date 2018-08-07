import os
import fnmatch
from textblob import TextBlob
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import regex as re
import operator
from sklearn.svm import SVC, LinearSVC
from sklearn import metrics
from sklearn import svm
from sklearn.grid_search import GridSearchCV
import pickle
from nltk.corpus import stopwords

path = 'op_spam_v1.4/'

label = []

configfiles = [os.path.join(subdir,f)
for subdir, dirs, files in os.walk(path)
    for f in fnmatch.filter(files, '*.txt')]

len(configfiles)

configfiles[1]

for f in configfiles:
    c = re.search('(trut|deceptiv)\w',f)
    label.append(c.group())

labels = pd.DataFrame(label, columns = ['Labels'])

labels.head(5)

review = []
directory = os.path.join('op_spam_v1.4')
for subdir, dirs, files in os.walk(directory):
    print(subdir)
    for file in files:
        if fnmatch.filter(files, '*.txt'):
            f = open(os.path.join(subdir, file), 'r')
            a = f.read()
            review.append(a)

reviews = pd.DataFrame(review, columns = ['HotelReviews'])

reviews.head(5)

results = pd.merge(reviews, labels, right_index = True, left_index = True)

results['HotelReviews'] = results['HotelReviews'].map(lambda x: x.lower())
