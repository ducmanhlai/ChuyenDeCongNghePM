'''
CD3:  Probability estimates
N19DCCN046 - DANG HOANG HA
N19DCCN047 - DANG MINH HAI
N19DCCN106 - LAI DUC MANH
'''

from nltk.corpus import stopwords
import math
import re
import time

def createStore(stopWords):
    text = open('doc-text').read()
    text = text.lower()
    segments = text.split('\n   /\n')[:-1]
    word_dict = {}
    for i, segment in enumerate(segments):
        lines = segment.split('\n')
        segment_name = lines[0].strip()
        words = lines[1].split()
        for word in words:
            if word not in stopWords:
                if word not in word_dict:
                    word_dict[word] = []
                if segment_name not in word_dict[word]:
                    word_dict[word].append(segment_name)
    word_dict={k: word_dict[k] for k in sorted(word_dict)}
    return word_dict

def store(file,stopWords):
    text = open(file).read()
    text = text.lower()
    segments = text.split('/\n')[:-1]
    query_dict = {}
    for i, segment in enumerate(segments):
        lines = segment.strip().split('\n')
        segment_name = str(i + 1)
        words = lines[1].split()
        query_dict[segment_name] = [word for word in words if word not in stopWords]
    return query_dict

def findV(V):
    if V:
        print('a')
    else:



def main():
    # List stop words
    stop_words = set(stopwords.words('english'))

    # dict{docName/queryName: listword in doc/query}
    # docs_dict = store('doc-text', stop_words)
    queries_dict = store('query-text', stop_words)

    #inverted index dict{word not in stop word: [list doc name word appear]}
    word_dict = createStore(stop_words)


if __name__ == "__main__":
    main()