import sys
N=int(sys.stdin.readline().strip())

ss1="\"재귀함수가 뭔가요?\""
ss2=["\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n","마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n","그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""]
ss3="\"재귀함수는 자기 자신을 호출하는 함수라네\""
ss4="라고 답변하였지."
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
for i in range(N+1):
    print("____"*i+ss1)
    if i==N:print("____"*i+ss3)
    else: print(''.join(["____"*i+s2 for s2 in ss2]))
    
for i in range(N,-1,-1):
    print("____"*i+ss4)

#런타임 에러
'''def Recursion_1(N,ss1,ss2,ss3):
    if N==0: 
        print(ss1)
        print(ss3)
    else:
        print(ss1)
        print(''.join(ss2))
        ss1="____"+ss1
        ss2=["____"*i+s2 for s2 in ss2]
        ss3="____"+ss3
        Recursion_1(N-1,ss1,ss2,ss3)
ss4="라고 답변하였지."
def Recursion_2(N,ss4):
    if N==0: print(ss4)
    else:
        print("____"*N+ss4)
        Recursion_2(N-1,ss4)
    

Recursion_1(N,ss1,ss2,ss3)
Recursion_2(N,ss4)'''