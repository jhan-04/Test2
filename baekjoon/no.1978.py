import sys
import math
N=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
div=list(range(2,round(math.sqrt(max(num))+1)))
prime=list(range(2,max(num)+1))

while div:
    prime=[i for i in prime if (i%div[0]!=0)or(i==div[0])]
    div=[i for i in div if (i%div[0]!=0)]
print(sum([1 for n in num if n in prime]))
     