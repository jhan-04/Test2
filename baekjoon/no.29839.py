import sys
N=int(sys.stdin.readline())# input() 과 동일
for i in range(1, N//3+1):
    cases=[[n, i-n] for n in range(i+1)]
    kg=[case[0]*3+case[1]*5 for case in cases]
    #print('case=',cases,'\n','kg=',kg)
    if N in kg: 
        print(i)
        break
    elif i==(N//3): print(-1)