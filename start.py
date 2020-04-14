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
# f.write can write backj in file if file is opend in write mode





