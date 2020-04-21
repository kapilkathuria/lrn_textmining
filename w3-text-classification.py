# Key Concepts
# Compare text classification to other classification approaches 
#   (covered in Applied Machine Learning in Python as well)
# Describe the Naive Bayes and Support Vector Machine algorithms
# Classify text in two classes using one of these approaches in Python
# Identify and extract features from text and transform them into 
#   feature vectors for the machine learning models

# Types of Textual Features
# A) Words: most common class of words. English language has 40,000 words
#   hence 40,000 features are added.
#   hence you need to add stop words
#   1. Stop Words: as these words don't add vaues to classification
#   2. Normalization: should you make lower case or leave as it is
#   3. Stemming and Lemmatization

# B) Characteristics fo Words: Capitilization
# C) POS Tagging
# D) Grammatical Structure
# E) Grouping Similar words together of similar meaning and semntics
#   ex. {buy, purchage} or {Mr. Mrs. Prof.}; Numbers / Digits; Dates
#   you might want to all numbers as 'Numbers' and all dates as 'dates'
# F) Domain Words: ?
# G) bi-grams, trigrams, n-grams: "White House"



# ---------------Using NAIVE BAYES------------------
# use case: Classifyin text search queries
# 3 classes: entertainment, computer science, zoology
# most common class is entertainment
# but if 'Python' word appears, most likely this will zoology as it is most common
# but if word is 'Python download' - it will be computer science

# Naive Bayes: Prior probablity - sum of all probabllities is 1.
# Posterior probablity
# Bayes Theorm - Posterior probablity = (Prior probability x Likelihood) / Evidence
# P(y|X) = P(y) x P(X|y) / P(x)

# Naive bayes is interested in 
# y* = argmax P(y|X) i.e. agument or computatin which maximizes probablity of y give X

# Naive Assumption: given the class Label, features are assumed to independent

# What are the parameters
# Prior probablity: P(y)
# Likelihood: P(X|y)
# see quiz in Video of Naive Bayes at around 11min

# Naive Bayes : Smoothing
# What if P(X|y) = 0??? ==> probably of P(y|X) will become zero
# this is where Smoothing helps
# so, we add dummy count i.e. let's is it  - it's nevver the case when countn is zero

# It is called Naive - because it assumes that features are independent of each other

# TRADITIONALLY THIS IS THE FIRST MODEL YOU SHOULD TRY


# Naive Bayes Patterns - 
# Multinomial: Assume that data follows multinomial distribution. We assume that each word is repeated 
#   few number of times
# Burnoulli: Assumes each feature is present or not present. Doesn't matter howo many 
#   times feature appears

# SUGGESTION: It is common to use Multinnomial for texxt classificatin but if you think
#   frequency doesn't matter, one can use Burnoulli as well.


# ---------------------TF-IDF: Term Frequency - Inverse Docment Frequency ---------------------
#   How common is this word? If word is occuriing more times, you might end up giving
#   moore weightage. TFIDF helps you more weightage to words which are not occuring 
#   those many times but are important


# ---------------------Support Vector Machine------------------------------------
# Classifier = Function of input data = F(X)
# Decision Bounderies: Support vector tries to create Bounderies
# Chossing a decison boundry: 
#   Linear (Planes / Hyper-Planes): Idea of using simmple model is called Occam's Razor.
#   there can be n number of llines which separate two classes but one that maximizes the disance
#   between boundry and points, is one we are looking for - this idea is called Maximum Margin.
# 
# How to find bounderies: Linear Classifiers and non-liner classifiers
# 
# SVM for multiclass classificcation: 
#   1. using one vs. rest, similary we learn all othe classes.
#   i.e. for n classes, we learn n classifiers.
#   2. Another approaches is One vs. One

# SVM Parameters: 
#   1. Parameter C - Regularization: How important is indivdual data point? Default Value is 1 i.e.
#       overall model should be simple and individual data point don't matter much
#   2. Kernerls: Linear vs non-linear
#   3. multi_class: ovr (one vs rest)
#   4. class_weight: Skewed Distribution - 

# Key POINTS
#   1. Tend to be MOST Accurate
#   2. Handles only numberical features. Hence categorical features need to be converted to numeric
#   3. Convert all numbers between range of 0-1
#   4. Hyper-planes are hard to interpret

