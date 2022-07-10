def solution(s):
    s=list(s)
    i=1
    while 1:
        if s[i-1]==s[i]:
            del s[i-1:i+1]
            if i>1:
                i-=1
        else:
            i+=1
        if i>=len(s):
            break

    return 1*(len(s)==0)