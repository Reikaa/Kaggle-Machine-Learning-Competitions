__author__ = 'Ahmed Hani Ibrahim'

from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn import svm
from get_data import *
from get_data_2 import *
from sklearn.feature_extraction.text import CountVectorizer
import scipy.sparse
import csv

ls = svm.LinearSVC()
labels, training_data_matrix, unique_ingredients = get_training_data_matrix(get_train_data())
ls = ls.fit(training_data_matrix, labels)

print("Training Done")

print(cross_val_score(ls, training_data_matrix, labels, cv=5).mean())

print("CV done")

test_data, ids = get_test_data()
test_data_matrix = get_test_data_matrix(test_data, unique_ingredients)

res = ls.predict(test_data_matrix)
print("Predicting Done")
submission = dict(zip(ids, res))

wr = csv.writer(open('Linear_SVC_Result.csv', 'wb'))
wr.writerow(['id', 'cuisine'])

for first, second in submission.items():
    wr.writerow([first, second])

print("done")
