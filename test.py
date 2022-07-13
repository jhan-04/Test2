#split
a='I and you'
print(a.split(' '))
t = 'MON TUE WED THU FRI SAT SUN'.split() #하나씩 리스트 작성 필요X

#3진수 to 10진수
a= 11
print(int(str(a),3))

#dictonary
dic={1: 'one', 'two':2}
print('1:',dic[1],'\t two:',dic['two'])
dict = {'김철수': 300, 'Anna': 180}
for key, value in dict.items():
    print(key, value) #김철수 300 Anna 180

# list in list
l=[[1,2,3], [2,3,5]] 
print(len(l[0]))

for i,j,k in l:
    print('i,j,k=',i,j,k)
for ll in l:
    print('ll=',ll)

#문자열에서 문자 위치
a = "Python is the best choice"
a.find('b') #14
a.index('t') #2

# 문자열 바꾸기
a = "Life is too short"
a.replace("Life", "Your leg") #'Your leg is too short'

#수식 to int
print(eval("1+2")) #3

#문자 대문자 소문자
a = "Hi"
a.upper() #HI
a.lower() #hi

#문자 삽입
",".join('abcd') #'a,b,c,d'
",".join(['a', 'b', 'c', 'd'])

#slice
ll=[1,2,3,4,5]
print(ll[:3]) #[1,2,3]
print(ll[1:3]) #[2,3]

#index
a = [3,6,1,2]
a.index(3) #0

#enumerate는 (index, 값) 
for entry in enumerate(['A', 'B', 'C']):
    print(entry) #(0, 'A') (1, 'B') (2, 'C')
for i, letter in enumerate(['A', 'B', 'C']):
    print(i, letter) #0 A  1 B  2 C

#zip
a=[1,2,3]
b=[4,5,6]
print(list(zip(a,b))[1][1]) #[1]->(2,5), [1][1]->5

for x, y in zip(range(10), range(10)):  # 두개의 0~9까지 숫자모음
    print(x, y) #0,0 1,1 2,2 ~~~

#삭제 del remove pop
a = [1,2,3,4,5]
del a[1] #a=[1,3,4,5] index로 삭제
a.remove(3) #a=[1,4,5] 값으로 삭제
a.pop(0) # a=[4,5] index로 삭제

##모든 요소 제거
numbers=[1,2,3,4,3,3,1,3]
for _ in numbers: 
    numbers.remove(3)


#정렬 sorted sort reversed revers
print(sorted([4,5,1,6,3]))
s=[4,5,1,6,3]
print(list(reversed(s)))
s.sort()
s.reverse()
print(s)



#빈 list 숫자 추가
answer = []
answer.append(1) #answer+=1 #동작X






