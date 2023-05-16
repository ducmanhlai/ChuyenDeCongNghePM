'''
CD2: the vector space model
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
                word_dict[word].append(segment_name)
    word_dict={k: word_dict[k] for k in sorted(word_dict)}
    return word_dict

def queryStore(stopWords):
    text = open('query-text').read()
    text = text.lower()
    segments = text.split('/\n')[:-1]
    query_dict = {}
    for i, segment in enumerate(segments):
        lines = segment.strip().split('\n')
        segment_name = str(i + 1)
        words = lines[1].split()
        query_dict[segment_name] = [word for word in words if word not in stopWords]
    return query_dict

def docStore(stopWords):
    text = open('doc-text').read()
    text = text.lower()
    segments = text.split('\n   /\n')[:-1]
    doc_dict = {}
    for i, segment in enumerate(segments):
        lines = segment.strip().split('\n')
        segment_name = str(i + 1)
        words = lines[1].split()
        doc_dict[segment_name] = [word for word in words if word not in stopWords]
    return doc_dict

def tf(store):
    dict = {}
    subDict = {}
    for doc in store:
        for word in store[doc]:
            count = store[doc].count(word)
            subDict[word] = 1 + math.log10(count)
            print(word)
            print(count)
            print(store[doc])
            time.sleep(1)
        dict[doc] = subDict
    return dict

def idf(word_dict, N):
    dict = {}
    for key in word_dict:
        dict[key] = math.log10(N/len(word_dict[key]))
        # print(key)
        # print(word_dict[key])
        # print(len(word_dict[key]))
        # time.sleep(5)
    return dict

def main():
    stop_words = set(stopwords.words('english'))
    doc_dict = docStore(stop_words)
    word_dict = createStore(stop_words)
    N = len(doc_dict)
    print(tf(doc_dict))
    time.sleep(5)


if __name__ == "__main__":
    main()