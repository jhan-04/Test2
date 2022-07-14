import sys
N=int(sys.stdin.readline())
lis=['']*N
case={}
for i in range(N):
    lis[i]=sys.stdin.readline().strip()
lis=list(set(lis))
lenth=[len(x) for x in lis]

case=(sorted(sorted(lis), key=lambda x:(len(x),x))) # key=len 도 통과가능
for x in case: print(x)