# Learning text mining
# Course https://www.coursera.org/learn/python-text-mining/home/welcome

# Week 1 - Working with Text in Python

# Parse / Find / Indetify / Extract 
# Classify / Sentiment
# Topic Modelling

# Premitive constructs - sentences --> Words--> Chartacters

text1 = "Kapil is learning text mining Mining IS"
print(len(text1))

# Tockens
print("Tokens")
text2 = text1.split(' ')
print(text2)

# unique words
print("Unique Words")
print(set([w.lower() for w in text2]))

# Word Comparision
print(text1.startswith("Kapil"))
print(text1.endswith("is"))
print("mining"in text1)
print(text1.islower())
print(text1.isalpha())
print(text1.isdigit())
print(text1.isalnum())
# print(text1.islower())

# String Operstiion
print("------------------String Operation--------------------")
print(text1.lower())
print(text1.title())
print(text1.splitlines())
print(text1.join("he"))
print(text1.strip())
print(text1.rfind("mining"))
print(text1.replace("mining","nomon"))

# Words to Chars
print("------------------Words to Chars--------------------")
capital = 'ouagadougou'
print(capital.split('ou'))
print('ou'.join(capital.split('ou')))
print(list(capital))
print([c for c in capital])

# Text Cleaning
print("------------------Text Cleaning--------------------")
sentence = '    A quick brown fox jumpedover the lazy dog.  '
print(sentence.split(' '))
print(sentence.strip().split(' '))
print(sentence.find('o'))
print(sentence.rfind('o'))
print(sentence.replace('o','O'))


# Larger Text
print("------------------Larger Text--------------------")
f = open('largefile.txt','r')
print(f.readline())

# Read Full file
print(f.seek(0))    # Sets the pointner back to 0
text12= f.read()
print(len(text12))
# print(text12.splitlines())      #Create a array with each line as item
print(len(text12.splitlines()))     # Number of Lines
text13 = text12.splitlines()
print(text13[0])
f.close()
# f.write can write back in file if file is opend in write mode

# ------------------------------Regular expression--------------------------
tweet_unsg = '"Ethics are built rilght into the ideals nd objectives of the United Natioins" \
    #UNSG #Women 2 NY Society for Ethical Culture bit.ly/2guVelr @UN @UN_Women'

tweet_token = tweet_unsg.split(' ')
print (tweet_token)

# All Hashtags
print([word for word in tweet_unsg.split() if word.startswith('#')])

# Callout
print([word for word in tweet_unsg.split() if word.startswith('@')])
# but this may return wrong some time
# Let's try Regex

# Let's learn regex
# . : wildcard, matches a single character
# ^ : start of string
# $ : end of string
# [] : Match one of the character withinn it
# [a-z] : matches range a-z
# [^abc] : inverse. match any charaacter which is not a, b, c
# a|b : match either a or b
# () : Scoping for 
# \ : Escape Character
# \b : Mataches word boundry
# \d : match any digit = [0-9]
# \D: Any non-digit = [^0-9]
# \s: Any whitespace = [ \t\n\r\f\v]
# \S : invese of \s = [^ \t\n\r\f\v]
# \w = Alphanumeric = [a-zA-Z0-9]
# \W : Inverse of \w = [^a-zA-Z0-9_]

#Repitions
# * : Zero or more time
# + : One or more time but at least once
# ? : matches zero or 1 time
# {n} : exactly n times
# {n,} : atleast n times
# {,n} : at most n times
# (m,n): at least m times and at most n times

import re

# let's get callouts
print([word for word in tweet_unsg.split() if re.search('@\w+',word)])
# or
print([word for word in tweet_unsg.split() if re.search('@[_a-zA-Z0-9]+',word)])






