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
        words = []
        for i in range(0,len(lines)):
            if i ==0:
                segment_name = lines[i].strip()
            else:
                words.extend(lines[i].split())
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
        words = []
        for i in range(1,len(lines)):
            words.extend(lines[i].split())
        query_dict[segment_name] = [word for word in words if word not in stopWords]
    return query_dict

def Ct(V,s,S,n,N):
    if V:
        p = (s+0.5)/(S+1)
        r = (n - s + 0.5)/(N-S+1)
        c = math.log10((p*(1-r))/(r*(1-p)))
    else:
        c = math.log10((N - n + 0.5) / (n + 0.5))
    return c

# def simScore(queries_dict,docs_dict,word_dict):
#     dict = {}
#     V = []
#     for query in queries_dict:
#         for word in query:
#             c_query =
#     return dict






def main():
    # List stop words
    stop_words = set(stopwords.words('english'))

    # dict{docName/queryName: listword in doc/query}
    docs_dict = store('doc-text', stop_words)
    queries_dict = store('query-text', stop_words)

    #inverted index dict{word not in stop word: [list doc name word appear]}
    word_dict = createStore(stop_words)

    N = len(docs_dict)




if __name__ == "__main__":
    main()