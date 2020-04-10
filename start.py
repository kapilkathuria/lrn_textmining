# Learning text mining
# Course https://www.coursera.org/learn/python-text-mining/home/welcome

# Week 1 - Working with Text in Python

# Parse / Find / Indetify / Extract 
# Classify / Sentiment
# Topic Modelling

# Premitive constructs - sentences --> Words--> Chartacters

text1 = "Kapil is learning text mining"
print(len(text1))

# Tockens
text2 = text1.split(' ')
print(text2)

# Find Specific
print(w for w in text2)

