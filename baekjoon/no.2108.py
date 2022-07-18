#시간초과
import sys
N=int(sys.stdin.readline())
nums=[0]*N
for i in range(N):
    nums[i]=int(sys.stdin.readline())
nums.sort()
print(round(sum(nums)/N))
print(nums[N//2])
answer4=nums[-1]-nums[0]
cnt=0
num_set=list(set(nums))
for i in range(len(num_set)-1,-1,-1):
    if nums.count(num_set[i])<cnt: 
        num_set.remove(num_set[i])
    elif nums.count(num_set[i])>cnt:
        cnt=nums.count(num_set[i])
        del num_set[i+1:] 
        
if len(num_set)==1:print(num_set[0])
else: print(sorted(num_set)[1])
print(answer4)