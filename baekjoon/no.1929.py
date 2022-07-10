#런타임에러
import sys
import math
M,N= map(int,sys.stdin.readline().split())
list=[i for i in range(M,N+1)]
no_num=[]
num=[]
i=1
while i<N:
    i+=1
    if i not in no_num:
        no_num=no_num+[i*k for k in range(1,N//i+1)]
        if i>=M: num.append(i)
print(num)


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