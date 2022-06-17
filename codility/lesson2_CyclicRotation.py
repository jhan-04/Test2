# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    AA=A*2
    sol=[AA[i-(K%len(A))] for i in range(len(A)) ]
    # write your code in Python 3.6
    return sol

#https://app.codility.com/demo/results/trainingSPQ6NB-9AS/