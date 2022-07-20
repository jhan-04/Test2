import sys
N=int(sys.stdin.readline())
nums=[]
for i in range(N):
    nums.append(tuple(map(int, sys.stdin.readline().split())))
nums=sorted(nums, key=lambda x:(x[0],x[1]))
for num in nums:
    print(num[0],num[1])