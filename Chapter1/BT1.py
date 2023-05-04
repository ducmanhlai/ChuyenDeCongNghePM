def createStore():
    f = open("doc-text", "r")
    dic=dict()
    posting =1
    for i in f:
        for j in i.split():
            j=  j.lower()
            if (j.isnumeric()):
                posting=int(j)
            else:
                if dic.get(j) is None:
                    dic.update({j:[posting]})
                else:
                    if posting not in dic[j]:
                        dic[j].append(posting)
    return dic
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
# a= createStore()
# print(a.get('create'))
kq= Intersect([1,2,3,4,5],[1,3,5])
print(kq)