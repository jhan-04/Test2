import sys
N=int(sys.stdin.readline().strip())
cnt=0
case=[N]
while 1:
    if 1 in case: break
    cnt+=1
    test=[]
    for i in range(len(case)):
        a=case[i]
        if a%6==0: 
            test.append(a//3)
            test.append(a//2)
        elif a%3==0: 
            test.append(a//3)
        elif a%2==0: 
            test.append(a//2)
        test.append(a-1)
    case=test
print(cnt)