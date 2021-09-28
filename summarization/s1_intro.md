course: https://www.udemy.com/course/text-summarization-natural-language-processing-python

course contents: summarization: take a wiki article and summarize that
1. frequency based
2. luhn algorithm
3. cosine similarity
4. libraries: sumy, pysummarization, bert summarizer
5. two way to generate summary: adstactive and extractive. in this course we focus on extractive. i.e. we extract the text but we don't change the extract. abstractive techniques will create news text like one has read and summarized in their own language

all course will implemented in google colab.

prerequisite


----------------- 
below is not from course

https://www.youtube.com/watch?v=pTHBZ6AyzOg - Summarize Written Text using Google's BERT | Machine Learning | Deep Learning

Code: of youtube video: https://github.com/bhattbhavesh91/text-summarizer-using-BERT 

library: https://github.com/dmmiller612/bert-extractive-summarizer

Bert Extractive Summarizer : This repo is the generalization of the lecture-summarizer repo. This tool utilizes the HuggingFace Pytorch transformers library to run extractive summarizations. This works by first embedding the sentences, then running a clustering algorithm, finding the sentences that are closest to the cluster's centroids. This library also uses coreference techniques, utilizing the https://github.com/huggingface/neuralcoref library to resolve words in summaries that need more context. The greedyness of the neuralcoref library can be tweaked in the CoreferenceHandler class.
