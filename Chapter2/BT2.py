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


#input doc/query in type listword
def tfidf(list,idf):
    dict = {}
    for word in list:
        if word not in dict:
            if word not in idf:
                dict[word]=0
            else:
                count = list.count(word)
                tf = (1 + math.log10(count))
                word_tfidf = tf * idf[word]
                dict[word] = word_tfidf
    return dict

#function finding idf
def idf(word_dict, N):
    dict = {}
    for key in word_dict:
        S = math.log10(N/len(word_dict[key]))
        dict[key] = S
    return dict

def lengthQD(Wq,Wd):
    length, a, b = 0, 0, 0
    for q in Wq:
        a = a+(Wq[q]*Wq[q])
    for d in Wd:
        b = b+(Wd[d]*Wd[d])
    length = math.sqrt(a*b)
    return  length

def simScore(queries_dict,docs_dict,word_idf):
    dict = {}
    for query in queries_dict:
        tfidf_query = tfidf(queries_dict[query], word_idf)
        subDict = {}
        for doc in docs_dict:
            score = 0
            tfidf_doc = tfidf(docs_dict[doc],word_idf)
            lengthQD(tfidf_query, tfidf_doc)
            for w in tfidf_query:
                if w not in tfidf_doc:
                    score = score
                else:
                    score = score + (tfidf_query[w] * tfidf_doc[w])
            subDict[doc] = score
        dict[query] = subDict
    return dict

def main():
    #List stop words
    stop_words = set(stopwords.words('english'))
    result = open("Vector_Space", "w")


    #dict{docName/queryName: listword in doc/query}
    docs_dict = store('doc-text',stop_words)
    queries_dict = store('query-text',stop_words)

    #inverted index dict{word not in stop word: [list doc name word appear]}
    word_dict = createStore(stop_words)

    N = len(docs_dict)

    #idf of list word in inverted index word_idf{word: idf value}
    word_idf = idf(word_dict,N)

    score = simScore(queries_dict,docs_dict,word_idf)

    for query in score:
        result.writelines(f"{query} \n")
        sorted_items = sorted(score[query].items(), key=lambda x: x[1], reverse=True)
        top_10 = sorted_items[:10]
        for doc in top_10:
            result.writelines(f"    {doc}    ")
        result.writelines(f"\n  \ \n")


if __name__ == "__main__":
    main()