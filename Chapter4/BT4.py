from nltk.corpus import stopwords
import math
import numpy as np
b=0.5

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
def count(doc,word):
    tmp=0
    for i in doc:
        if(i==word): 
            tmp+=1
    return tmp
def RSV(N,querie,docs_dict,word_dict,doc):
    k=2
    total=0
    avdl =Avdl(docs_dict)
    for i in querie:
        tfi= count(doc,i)
        nqi=len(word_dict[i])
        idf= math.log2((N-nqi+0.5)/(nqi+0.5))
        if tfi>0:
            Ci= idf*((k+1)*tfi/(k*(1-b+b*len(doc)/avdl)+tfi))
            total+=Ci
    return total
def Score(N,queries_dict,docs_dict,word_dict):
    for i in queries_dict:
        tmp=np.zeros(N)
        for j in range(1,N):
           scr= RSV(N,queries_dict[i],docs_dict,word_dict,docs_dict[str(j)])
           tmp[j]=scr
        top_10_indices = np.argsort(tmp)[-20:]
        print(i,": ",top_10_indices)
def Avdl(docs_dict):
   tmp=0
   for i in docs_dict:
       tmp+=len(docs_dict[i])
   return tmp/len(docs_dict)
def main():
    stop_words = set(stopwords.words('english'))
    #dict{docName/queryName: listword in doc/query}
    docs_dict = store('doc-text',stop_words)
    queries_dict = store('query-text',stop_words)
    #inverted index dict{word not in stop word: [list doc name word appear]}
    word_dict = createStore(stop_words)
    N = len(docs_dict)
    # N=7000 
    # print(Avdl(docs_dict))
    Score(N,queries_dict,docs_dict,word_dict)
if __name__ == "__main__":
    main()
