from itertools import permutations
def solution(numbers):
    numbers=[str(i) for i in numbers]
    lis=list(map(int,map(''.join,permutations(numbers,len(numbers)))))
    answer = ''
    print(lis)
    return answer


solution([6,10,2])