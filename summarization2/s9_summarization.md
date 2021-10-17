course: https://www.udemy.com/course/awesome-natural-language-processing-tools-in-python

# video 77
extractive : text extracted from exisitng
abstractive: new text created. computationally more challenging. it builds internal semantic representation of th eorignial contnet, and then use this reperesentaion to crate a summary that is close to twhat a human might express

# video 78 - evaluation of text summarization
1. BLUE: bilingiual evaluation understudy. measures precision. originally created for machine translation. compares the ngram of sample result.
drawbacks
a) doesn't cosnider meaning
b) doesn't consider sentence structure
c) doesn't handle morphologically rich language
2. Rouge: recall oriented understudy. measures recall. find n-grams similar in labelled data. Rouge N - where N is n-gram

# video 79 - libraries
different libraties
1. nltk: word frequency / bag of words
2. spacy: word frequency / bag of words
3. sumy, summa
4. transformers: mostly for extractive. seq2seq

differrent methodologies
1. word frequency
2. lsa
3. text rank
4. lex rank
5. seq2seq: BERT

# 80 - extractive with sumy