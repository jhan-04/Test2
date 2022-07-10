N,K= input().split()
N=int(N)
K=int(K)
degree=input().split()

dgree=[int (i) for i in degree]
K_sum=[] 
for i in range(N-K+1):
    K_sum.append(sum(dgree[i:i+K]))
    
print (int(max(K_sum))) 