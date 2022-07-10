import sys
N=int(sys.stdin.readline())
stack=[]
for i in range(N):
    order=sys.stdin.readline().replace('\n','')
    if 'push' in order:
        stack.append(order[5:])
    elif 'pop' in order:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif 'size' in order:
        print(len(stack))
    elif 'empty' in order:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif 'top' in order:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])