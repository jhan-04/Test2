
#N=10 #sol=29
#M=13
#table=['BBBBBBBBWBWBW','BBBBBBBBBWBWB','BBBBBBBBWBWBW','BBBBBBBBBWBWB','BBBBBBBBWBWBW','BBBBBBBBBWBWB','BBBBBBBBWBWBW','BBBBBBBBBWBWB','WWWWWWWWWWBWB','WWWWWWWWWWBWB']
#N=11 #sol=15
#M=12
#table=['BWWBWWBWWBWW','BWWBWBBWWBWW','WBWWBWBBWWBW','BWWBWBBWWBWW','WBWWBWBBWWBW','BWWBWBBWWBWW','WBWWBWBBWWBW','BWWBWBWWWBWW','WBWWBWBBWWBW','BWWBWBBWWBWW','WBWWBWBBWWBW']

#N=9 #sol=29
#M=9
#table=['BBBBBBBBB', 'WWWWWWWWW','WWWWWWWWW','WWWWWWWWW','WWWWWWWWW','WWWWWWWWW','WWWWWWWWW','BWWWWWWWW','WWBWBWBWW']

N,M=input().split()
N=int(N)
M=int(M)
table=['']*N
for i in range(N):
    table[i]=input()

sol=M*N
for i in range(N-7):
    for j in range(M-7):
        start1='W'
        start2='B'
        cnt_1=0
        cnt_2=0
        for r in range(i,i+8):
            for c in range(j,j+8):
                if ((r+c)%2==0 and table[r][c]!=start1) or ((r+c)%2!=0 and table[r][c]==start1):
                    cnt_1+=1
                if ((r+c)%2==0 and table[r][c]!=start2) or ((r+c)%2!=0 and table[r][c]==start2):
                    cnt_2+=1
                    
        sol=min(sol,cnt_1,cnt_2)
print(sol)