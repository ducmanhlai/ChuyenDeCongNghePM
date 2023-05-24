from nltk.corpus import stopwords
import math
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
    word_dict = {k: word_dict[k] for k in word_dict}
    return word_dict


def store(file, stopWords):
    text = open(file).read()
    text = text.lower()
    segments = text.split('/\n')[:-1]
    query_dict = {}
    for i, segment in enumerate(segments):
        lines = segment.strip().split('\n')
        segment_name = str(i + 1)
        words = lines[1].split()
        query_dict[segment_name] = [
            word for word in words if word not in stopWords]
    return query_dict
def count(doc,word):
    tmp=0
    for i in doc:
        if(i==word): tmp+=1
    return tmp
def RSV(N,querie,docs_dict,word_dict):
    scrore= []
    for i in querie:   
        for j in word_dict:
         Cj=math.log2(N/len(docs_dict[i]))*(3*count(i,j))
def Score(N,queries_dict,docs_dict,word_dict):
    tmp=[]
    print(queries_dict)
    for i in queries_dict:
        RSV(N,queries_dict[i],docs_dict,word_dict)
        tmp.append({})
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
    print(Avdl(docs_dict))   
    # Score(N,queries_dict,docs_dict,word_dict)
if __name__ == "__main__":
    main()
