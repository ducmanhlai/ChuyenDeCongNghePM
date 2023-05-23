from nltk.corpus import stopwords

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
        query_dict[segment_name].sort()
    return query_dict

def Intersect(li1,li2):
    result =[]
    pos1=0
    pos2=0
    while pos1<len(li1) and pos2<len(li2):
        if li1[pos1]==li2[pos2]:
            result.append(li1[pos1])
            pos1+=1
            pos2+=1
        else:
            if li1[pos1]<li2[pos2]: pos1+=1
            else: pos2+=1
    return result

def IntersectWithSkip(li1, li2, skip=1):
    result = []
    pos1 = 0
    pos2 = 0
    skip= int(abs(min(len(li1),len(li2))))
    print(skip)
    while pos1 < len(li1) and pos2 < len(li2):
        if li1[pos1] == li2[pos2]:
            result.append(li1[pos1])
            pos1 += 1
            pos2 += 1
        else:
            if li1[pos1] < li2[pos2]:
                if (skip+pos1<len(li1)) and li1[pos1+skip]<=li2[pos2]:
                    while (skip+pos1<len(li1)) and li1[pos1+skip]<=li2[pos2]:
                        pos1+=skip
                else: pos1+=1
            else:
                if (skip+pos2<len(li2)) and li2[pos2+skip]<=li1[pos1]:
                    while (skip+pos2<len(li2)) and li2[pos2+skip]<=li1[pos1]:
                        pos2+=skip
                else: pos2+=1
    return result


def booleanQuery(query, doc_list):
    result = []
    # print(query)
    for term in query:
        # print(term)
        if not result:
            result = doc_list.get(term, [])
        else:
            result = Intersect(result, doc_list.get(term, []))
    return result

def booleanQueryWithSkip(query, doc_list):
    result = []
    # print(query)
    for term in query:
        # print(term)
        if not result:
            result = doc_list.get(term, [])
        else:
            result = IntersectWithSkip(result, doc_list.get(term, []))
    return result

def main():
    stop_words = set(stopwords.words('english'))
    queries = queryStore(stop_words)
    doc = createStore(stop_words)
    resultBooleanQuery = open("booleanQuery", "w")
    resultBooleanQueryWithSkip = open("booleanQueryWithSkip", "w")

    for query, terms in queries.items():
        result = booleanQuery(terms, doc)
        # print(f"Query '{query}' matched documents: {result}")
        resultBooleanQuery.writelines(f"{query} \n")
        resultBooleanQueryWithSkip.writelines(f"{query} \n")
        for a in result:
            resultBooleanQuery.writelines(f"    {a}    ")
            resultBooleanQueryWithSkip.writelines(f"    {a}    ")
        resultBooleanQuery.writelines(f"\n  \ \n")
        resultBooleanQueryWithSkip.writelines(f"\n  \ \n")


if __name__ == "__main__":
    main()