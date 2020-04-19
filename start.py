# Learning text mining
# Course https://www.coursera.org/learn/python-text-mining/home/welcome

# Week 1 - Working with Text in Python

# Parse / Find / Indetify / Extract 
# Classify / Sentiment
# Topic Modelling

# Premitive constructs - sentences --> Words--> Chartacters

# -------------------Section Resources------------------------------------
# Regular Exprreessions
# Regular expressions documentation in Python 3
# Tips and tricks of the trade for cleaning text in Python
# https://stanford.edu/~rjweiss/public_html/IRiSS2013/text2/notebooks/cleaningtext.html
# https://www.analyticsvidhya.com/blog/2014/11/text-data-cleaning-steps-python/
# http://ieva.rocks/2016/08/07/cleaning-text-for-nlp/
# https://chrisalbon.com/python/cleaning_text.html
# ------------------------------------------------------------------------------------------

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
print([word for word in tweet_unsg.split() if re.search(r'@\w+',word)])
# or
print([word for word in tweet_unsg.split() if re.search('@[_a-zA-Z0-9]+',word)])

# Find specific character
print(re.findall(r'[aeiou]', capital))

print(re.findall(r'[^aeiou]', capital))

# Regular Variation for Dates
# To Match many variation of date

datestr = "21 Jan 2009, 21/01/2009, 21/01/09, Jan 21 2009, 2009-01-09, 21 January 2009,  \
    January 21, 2009"

print(re.findall(r'(?:\d{2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{1,2}, )?\d{4}' \
, datestr))
print(re.findall(r'(?:\d{2} )(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*' , datestr))


# Regex with Pandas
# See https://rvtpxxltpgkzkhxqvzmbpo.coursera-apps.org/notebooks/Regex%20with%20Pandas%20and%20Named%20Groups.ipynb


# Multiple Language - internationlization

# ASCII - encoding for English
# 128 codes -- 7Bits
# It doesn't capture Diacitics 
# Many cities and organization use these Diacritics
# it doesn't cover other languages, emoji, music etc.
# 36% people use Latin, 2nd is CHinese

# Other encoding schemes
# IBM EBCDIC, Latin -1, EUC (Extended Unix Code)
# Unicode and UTF-8
# UTF is more than 60% now

# Unicode - 128K characters

# UTF -8
# Unicode Transformational formats 8 bits
# 1-4 bytes
# Backward code with ASCII - 1 byte code codes same
# default in python 3
# résumé - len in pyhton 3 shown in 6 while in python 2 is 8
# In python 2 you can say it is unicode by using (u'résumé')

