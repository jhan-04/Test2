num=list(range(1,10000))
lis=[]
i=0
for n in num:
    lis.append(n+sum(list(map(int,list(str(n))))))
answer=[i for i in num if i not in lis]
for i in answer: print(i)
    