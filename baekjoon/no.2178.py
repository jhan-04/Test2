# 다시 공부하고 해볼 것
import sys

'''def moving(x,y,table_map,load,fail):
    #동남서북
    x_move=[1,0,-1,0]
    y_move=[0,-1,0,1]
    for x_m,y_m in zip(x_move,y_move):
        if table_map[x+x_m][y+y_m]=='1' and ((x+x_m,y+y_m) not in fail):
            if (x,y) in load:
                load.remove((x,y))
                fail.append((x,y))
            else:
                load.append((x+x_m,y+y_m))    
            x=x+x_m
            y=y+y_m
    return x,y,load,fail'''


N,M= map(int, sys.stdin.readline().split())
table_map=[]

for _ in range(N):
    table_map.append(list(sys.stdin.readline().split()))
x_move=[1,0,-1,0]
y_move=[0,1,0,-1]
x,y=0,0
load=[(0,0)]
fail=[]
while x!=N-1 or y!=M-1:
    cnt=0
    for x_m,y_m in zip(x_move,y_move):
        if x+x_m>=0 and y+y_m>=0 and x+x_m<N and y+y_m<M:
            if table_map[x+x_m][y+y_m]=='1' and ((x+x_m,y+y_m) not in load) and ((x+x_m,y+y_m) not in fail):
                load.append((x+x_m,y+y_m))    
                x=x+x_m
                y=y+y_m
                break
            else: cnt+=1 
        else: cnt+=1
    if cnt==4: 
        load.remove((x,y))
        fail.append((x,y))
        x=load[-1][0]
        y=load[-1][1]
print(load)
print(len(load))
