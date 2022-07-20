import sys
N=int(sys.stdin.readline())
cnt=N
for n in range(N):
    word=list(sys.stdin.readline())
    for i in range(1, len(word)):
        if (word[i]!=word[i-1]) and (word[i] in word[:i]):
            cnt-=1
            break
print(cnt)        

