import os
import fnmatch
from textblob import TextBlob
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import regex as re
import operator
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn import metrics
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import pickle
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords

path = 'Machine_Learning/Deceptive_Hotel_Reviews/op_spam_v1.4/'

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
directory = os.path.join('Machine_Learning/Deceptive_Hotel_Reviews/op_spam_v1.4')
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

def svc_param_selection(X,y,nfolds):
    Cs = [0.001, 0.01, 0.1, 1, 10]
    gammas = [0.001, 0.01, 0.1, 1]
    param_grid = {'C': Cs, 'gamma' : gammas}
    grid_search = GridSearchCV(svm.SVC(kernel='linear'), param_grid, cv=nfolds)
    grid_search.fit(X, y)
    return grid_search.best_params_

svc_param_selection(X_train_tf, label_train, 5)

clf = svm.SVC(C=10, gamma=0.001, kernel='linear')
clf.fit(X_train_tf,label_train)
pred = clf.predict(X_test_tf)

with open('vectorizer.pickle', 'wb') as fin:
    pickle.dump(tf_vect, fin)

with open('mlmodel.pickle', 'wb') as f:
    pickle.dump(clf,f)

pkl = open('mlmodel.pickle', 'rb')
clf = pickle.load(pkl)
vec = open('vectorizer.pickle', 'rb')
tf_vector = pickle.load(vec)

X_test_tf = tf_vect.transform(review_test)
pred = clf.predict(X_test_tf)

print(metrics.accuracy_score(label_test, pred))
print(confusion_matrix(label_test, pred))

print(classification_report(label_test, pred))

#Random State 1

review_train, review_test, label_train, label_test = train_test_split(result['pos'], result['Labels'], test_size=0.2, random_state=1)
X_test_tf = tf_vect.transform(review_test)
pred = clf.predict(X_test_tf)

print(metrics.accuracy_score(label_test, pred))
print(confusion_matrix(label_test, pred))

print(classification_report(label_test, pred))

#Random State 10

review_train, review_test, label_train, label_test = train_test_split(result['pos'], result['Labels'], test_size = 0.2, random_state = 10)
X_test_tf = tf_vect.transform(review_test)
pred = clf.predict(X_test_tf)

print(metrics.accuracy_score(label_test, pred))
print(confusion_matrix(label_test, pred))

print(classification_report(label_test, pred))

#Random State 42

review_train, review_test, label_train, label_test = train_test_split(result['pos'], result['Labels'], test_size = 0.2, random_state = 42)
X_test_tf = tf_vect.transform(review_test)
pred = clf.predict(X_test_tf)

print(metrics.accuracy_score(label_test, pred))
print(classification_report(label_test, pred))

def test_string(s):
    X_test_tf = tf_vect.transform([s])
    y_predict = clf.predict(X_test_tf)
    return y_predict

test_string('The hotel was good. The room had a 27-inch Samsung led tv, a microwave. The room had a double bed')

array(['truth'], dtype = object)

test_string('My family and I are huge fans of this place. The staff is super nice, and the food is great. The chicken is very good, and the garlic sauce is perfect. Ice cream topped with fruit is delicious too. Highly recommend!')
