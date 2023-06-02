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

Doc_Text = 'doc-text'
Query_Text = 'query-text'

def createStore(stopWords):
    text = open(Doc_Text).read()
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

def store(file,stopWords,q='query-text'):
    text = open(file).read()
    text = text.lower()
    if file == q:
        segments = text.split('\n/\n')[:-1]
    else:
        segments = text.split('\n   /\n')[:-1]
    query_dict = {}
    for i, segment in enumerate(segments):
        lines = segment.strip().split('\n')
        segment_name = str(i + 1)
        words = []
        for i in range(1,len(lines)):
            words.extend(lines[i].split())
        query_dict[segment_name] = [word for word in words if word not in stopWords]
    return query_dict

def Ct_sau(n,N,s,S): # n:số lượng văn bản chứa từ, N:số lượng văn bản trong kho, s:số lượng văn bản chứa từ phù hợp Q, S:số lượng văn bản phù hợp
    p = (s + 0.5) / (S + 1)
    r = (n - s + 0.5) / (N - S + 1)
    c = math.log10((p * (1 - r)) / (r * (1 - p)))
    return c

def Ct_dau(n,N):
    c = math.log10((N - n + 0.5) / (n + 0.5))
    return c

# Tính RSV của doc theo query (output V[doc]:RSV)
def probability_estimates(N,query,word_dict,docs_dict,V=[],count=0): # V= {doc: RSV(doc,query)}
    C = {} # word: Ct
    V_now = {}
    if V: # nếu tập V (list doc phù hợp query) tồn tại
        for word in query:
            if word not in word_dict:
                n = 0
            else:
                n = len(word_dict[word])
            S = len(V)
            s=0
            for doc in V:
                if word in word_dict:
                    if doc in word_dict[word]:
                        s +=s
            C[word] = Ct_sau(n,N,s,S)

    else: # nếu tập V chưa có
        for word in query:
            if word not in word_dict:
                n = 0
            else:
                n = len(word_dict[word])
            C[word] = Ct_dau(n, N)

    for doc in docs_dict:
        RSV = 0
        for word in query:
            if word in docs_dict[doc]:
                RSV = RSV + C[word]
        V_now[doc] = RSV
    top_10= sorted(V_now, key=V_now.get, reverse=True)[:10]
    if top_10 == V:
        count+= 1
    else:
        count=0
    if count >=5:
        return top_10
    else:
        return probability_estimates(N,query,word_dict,docs_dict,top_10,count)

def run(N,word_dict,queries_dict,docs_dict):
    dict={}
    for query in queries_dict:
        list = probability_estimates(N,queries_dict[query],word_dict,docs_dict)
        dict[query]= list
    return dict

def main():
    # List stop words
    stop_words = set(stopwords.words('english'))

    # dict{docName/queryName: listword in doc/query}
    docs_dict = store('doc-text', stop_words)
    queries_dict = store('query-text', stop_words)

    #inverted index dict{word not in stop word: [list doc name word appear]}
    word_dict = createStore(stop_words)

    N = len(docs_dict)
    # print(docs_dict)
    result = run(N,word_dict,queries_dict,docs_dict)
    print(result)





if __name__ == "__main__":
    main()