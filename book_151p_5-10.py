N,M= map(int,input().split()) #세로, 가로

cases=[]
graph=[]*N
cnt=0
for i in range(N):
    a=list(map(int,input().split()))
    cases=cases+a
    graph.append(a)

def icecream(x,y):
    if x<0 or x>=M or y<0 or y>=N:
        return False
    if graph[y][x]==0:
        graph[y][x]=1
        cases[y*M+x]=1
        icecream(x-1,y)
        icecream(x,y-1)
        icecream(x+1,y)
        icecream(x,y+1)
        return True
    return False

while 0 in cases:
    x=(cases.index(0))%(M)
    y=(cases.index(0))//(M)
    if icecream(x,y)==True:
      cnt+=1
print(cnt)