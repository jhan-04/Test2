def solution(record):
    answer = []
    user={}
    for i in range(len(record)):
        if record[i].split(' ')[0]=='Enter' or record[i].split(' ')[0]=='Change':
            user[record[i].split(' ')[1]]=record[i].split(' ')[2]
    for i in range(len(record)):
        if record[i].split(' ')[0]=='Enter':
            answer.append(''.join([user[record[i].split(' ')[1]],"님이 들어왔습니다."]))
        elif record[i].split(' ')[0]=='Leave':
            answer.append(''.join([user[record[i].split(' ')[1]],"님이 나갔습니다."]))
    return answer

'''def solution(record):
    answer = []
    id_nic = {}
    for r in record:
        s = r.split()
        if len(s) > 2:
            id_nic[s[1]] = s[2]

    for r in record:
        s = r.split()
        if s[0] == "Enter":
            answer.append(id_nic[s[1]] + "님이 들어왔습니다.")
        elif s[0] == "Leave":
            answer.append(id_nic[s[1]] + "님이 나갔습니다.")
    return answer'''