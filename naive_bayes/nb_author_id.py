#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess 
from sklearn.naive_bayes import GaussianNB

#!/usr/bin/python
import numpy

# Load the variables from .npz file. Provide the path to the file
preprocessed = numpy.load("C:/Users/Aleena/Desktop/SEM6/Machine Learning/Projects/ud120-projects/preprocessed/preprocessed.npz")
# Create (global) variables from the loaded npz-file and assign names to them
for ii in preprocessed:
    globals()[ii] = preprocessed[ii]
# Delete the 'preprocessed' file since it's no longer needed
del preprocessed

# You can continue with the rest of your code her


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf=GaussianNB()
t0=time()
clf.fit(features_train,labels_train)
print ("training time:", round(time()-t0, 3), "s")
t0=time()
print(clf.predict(features_test))
print ("Predict time:", round(time()-t0, 3), "s")
print(clf.score(features_test,labels_test))


#########################################################


