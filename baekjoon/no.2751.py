import sys
N=int(sys.stdin.readline())
value=[0]*N
for i in range(N):
    value[i]=int(sys.stdin.readline())
value.sort()
for i in value: print(i)
    