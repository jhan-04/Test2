def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3) #tmp to 3진법
    return answer
    
    '''def solution(n):
    answer=0
    sol=[]
    while n!=0:
        sol+= str(n%3)
        n=n//3
    reversed(sol)
    for i in range(len(sol)):
        answer+=(3**i)*int(sol[-1-i])
    return answer'''