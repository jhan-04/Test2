import sys
T= int(sys.stdin.readline())
words=[]
for i in range(T):
    words.append(sys.stdin.readline().strip())
    
for word in words:
    while '()' in word:
        word=word.replace('()','')
    if len(word)==0: print('YES')
    else: print('NO')