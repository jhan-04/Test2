import sys
N,M= map(int,input().split())
dx=[0,1,0,-1]#북동남서
dy=[1,0,-1,0]

x,y,dir= map(int,input().split())
ground=[]
for i in range(N):
    ground.append(list(map(int,input().split())))
ground[x][y]=1
cnt=1
time=0
while 1:
    dir-=1 #시계반대방향으로 돌기
    if dir==-1: dir=3
    nx=x+dx[dir]
    ny=y+dy[dir]

    if ground[nx][ny]==0:
        ground[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        time=0
    else: time+=1

    if time==4:
        break
print(cnt)