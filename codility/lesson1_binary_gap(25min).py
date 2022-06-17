# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    bin_N=bin(N)
    max_len=0
    locate=[i for i in range(2,len(bin_N)) if int(bin_N[i])==1]
    for i in range(len(locate)-1):
        if max_len<(locate[i+1]-locate[i]-1):
            max_len=(locate[i+1]-locate[i]-1)
    return max_len



