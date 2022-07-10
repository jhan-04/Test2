K= int(input())
N=['']*K
M=['']*K

for i in range(K):
    N[i],M[i]= input().split()

N=list(map(int, N))
M=list(map(int, M))
#MCN
answer=[1]*K
for i in range(K):
    for j in range(1,N[i]+1):
        answer[i]*=(M[i]-j+1)
    for j in range(1,N[i]+1):
        answer[i]//=j
    print(answer[i])
