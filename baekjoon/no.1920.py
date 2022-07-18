
import sys
N=sys.stdin.readline()
lst1=sorted(list(sys.stdin.readline().split()))
M=int(sys.stdin.readline().strip())
lst2=list(sys.stdin.readline().split())

for x in lst2:
    ind_max=len(lst1)-1
    ind_min=0
    cnt=0
    while abs(ind_max-ind_min)>=1:
        if abs(ind_max-ind_min)==1: 
            if lst1[ind_max]==x or  lst1[ind_min]==x:
                print(1)
            else: print(0)
            break
        ind=(ind_max+ind_min)//2
        if lst1[ind]==x: 
            print(1)
            break
        elif lst1[ind]>x: ind_max=ind
        else: ind_min=ind


#https://wayhome25.github.io/cs/2017/04/15/cs-16/