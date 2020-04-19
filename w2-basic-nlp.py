# Learning text mining
# Course https://www.coursera.org/learn/python-text-mining/home/welcome

# Week 2 -- Module 2: Basic Natural Language Processing


# -------------------Section Resources------------------------------------
# 
# ------------------------------------------------------------------------------------------

# Natural language 
# language evolve

# NLP Tasks
# Counting Worlds
# Finding sentence bounderies
# Parsing Sentence Structure
# NER, Classification
# Coreference Resolution - which pronoun referes to which entity

import nltk

# download copora
# Run this in command prompt
# nltk.download()

from nltk.book import *
print(text7)
print(sents())

# WSJ Corpus 7
print(sent7)
print("Len of total corpus: " + len(text7))   
print("Unique words in corpus: " + len(set(text7)))
print("First 10 words in corpus:" + list(set(text7))[:10])

# Frequency Distribution