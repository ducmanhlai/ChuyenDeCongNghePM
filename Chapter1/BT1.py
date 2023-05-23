import nltk
from nltk.corpus import stopwords
listStopWord = stopwords.words('english')


def createStore():
    f = open("doc-text", "r")
    dic = dict()
    posting = 1
    for i in f:
        for j in i.split():
            j = j.lower()
            if (j.isnumeric()):
                posting = int(j)
            else:
                if dic.get(j) is None:
                    dic.update({j: [posting]})
                else:
                    if posting not in dic[j]:
                        dic[j].append(posting)
    return dic


def Intersect(li1, li2):
    result = []
    pos1 = 0
    pos2 = 0
    while pos1 < len(li1) and pos2 < len(li2):
            if li1[pos1] == li2[pos2]:
                result.append(li1[pos1])
                pos1 += 1
                pos2 += 1
            else:
                if li1[pos1] < li2[pos2]:
                    pos1 += 1
                else:
                    pos2 += 1
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


def readQuery():
    f = open("query-text", "r").read().splitlines()
    print(f)
    dic = dict()
    pos = 1
    for i in f:
        if i.isnumeric():
            pos = int(i)
            continue
        if i == '/':
            continue
        dic.update({str(pos): i.lower()})
    return dic


def rlv_ass():
    store = createStore()
    list_query = readQuery()
    for i in list_query:
        query = list_query.get(i)
        result = store.get(query.split()[0])
        for j in query.split():
            result = Intersect(result, store.get(j) if store.get(j) is not None else result)
        print(i+':  ', result)

# print(readQuery())
# rlv_ass()
a= createStore()
print(a)
# kq= Intersect([1,2,3,4,5],[1,3,5])
# print(kq)
# print(IntersectWithSkip([1,2,3,8,11,17,21,31],[2,4,8,41,48,64,128],))