
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer

#test1
new_id="...!@BaT#*..y.abcdefghijklm"
solution(new_id)

#mine
'''def solution(new_id):
    #step1
    new_id=new_id.lower()
    new_id=list(new_id)
    #step2
    removed=list("~!@#$%^&*()=+[{]}:?,<>/")
    removed_id=[x for x in new_id if x not in removed]
    
    #step3&4
    dots=[]
    if removed_id[0]=='.':
        dots.append(0)
    if removed_id[len(removed_id)-1]=='.':
        dots.append(len(removed_id)-1)
        
    for i in range(1, len(removed_id)):
        if removed_id[i]=='.' and removed_id[i-1]=='.':
            dots.append(i)
            if i==len(removed_id):
                dots.append(i-1)
    removed_id=[removed_id[x] for x in range(len(removed_id)) if x not in dots]

    
    #step5
    if len(removed_id)==0:
        removed_id.append('a')
    if len(removed_id)>=16:
        removed_id=removed_id[:15]
    if removed_id[-1]=='.':
            del removed_id[-1]
    if len(removed_id)<=2:
        while len(removed_id)<=2:
            removed_id.append(removed_id[-1])
    answer=''.join(removed_id)
    return answer '''