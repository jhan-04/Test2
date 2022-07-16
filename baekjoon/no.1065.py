import sys
N=int(sys.stdin.readline().strip())
if N<=99: print(N)
else:
    cnt=99
    for i in range(100,N+1):
        nums=list(map(int,list(str(i))))
        if len(set([nums[i]-nums[i+1] for i in range(len(nums)-1)]))==1:
            cnt+=1
    print(cnt)


