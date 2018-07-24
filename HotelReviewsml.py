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
