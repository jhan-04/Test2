#런타임에러
import sys
import math
M,N= map(int,sys.stdin.readline().split())
lis=list(range(M,N+1))
div=list(range(2,int(math.sqrt(N)+1)))
num=[]
i=1
while len(div):
    d=div[0]
    div=[i for i in div if (i%d!=0)]
    lis=[i for i in lis if (i%d!=0) or (i==d)]

if 1 in lis: del lis[0]
for n in lis: print(n)



#런타임에러
#import sys
#import math
#M,N= map(int,sys.stdin.readline().split())
#for num in range(M,N+1):
#    if num==1 or num==2:
#        print(num)
#    else:
#        test=[1 if num%i==0 else 0 for i in range(2,int(math.sqrt(num))+1)]
#        if sum(test)==0:
#            print(num)