# not done
N,M= input().split()
N=int(N)
M=int(M)
map=[]
for i in range(N):
    map.append(input())
    if 'R' in map[i]:
        Red=[i,map[i].index('R')]
        print(Red)
print(map)
