import sys
N=int(sys.stdin.readline().strip())
cnt=0
case=[N]
while 1:
    cnt+=1
    test=[]
    for i in range(len(case)):
        a=case[i]
        if a%3==0: 
            test.append(a//3)
        if a%2==0: 
            test.append(a//2)
        test.append(a-1)
    case=test
    if 1 in test: break
print(cnt)