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
from sklearn.cross_validation import train_test_split
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

result = pd.merge(reviews, labels, right_index = True, left_index = True)

result['HotelReviews'] = result['HotelReviews'].map(lambda x: x.lower())

result.head()

import nltk
nltk.download('stopwords')

stop = stopwords.words('english')

result['review_without_stopwords'] = result['HotelReviews'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

result.head()

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos(review_without_stopwords):
    return TextBlob(review_without_stopwords).tags

os = result.review_without_stopwords.apply(pos)
os1 = pd.DataFrame(os)
os1.head()

os1['pos'] = os1['review_without_stopwords'].map(lambda x:' '.join(['/'.join(x) for x in x]))

result = result = pd.merge(result, os1, right_index=True, left_index = True)
result.head()

review_train, review_test, label_train, label_test = train_test_split(result['pos'], result['Labels'], test_size=0.2, random_state=13)

tf_vect = TfidfVectorizer(lowercase = True, use_idf = True, smooth_idf = True, sublinear_tf = False)

X_train_tf = tf_vect.fit_transform(review_train)
X_test_tf = tf_vect.transform(review_test)
