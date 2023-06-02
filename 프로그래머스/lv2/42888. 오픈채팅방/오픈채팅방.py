def solution(record):
    answer = []
    nickname_dict = {}
    result = []
    do_tb = ['님이 들어왔습니다.', '님이 나갔습니다.']
    while record:
        line = record.pop().split()
        if line[0] == 'Enter' or line[0] == 'Change':
            if line[1] not in nickname_dict:
                nickname_dict[line[1]] = line[2]
        
        if line[0] != 'Change':
            do = 0 if line[0] == 'Enter' else 1
            result.append([line[1], do])
    
    while result:
        uid, do = result.pop()
        answer.append(nickname_dict[uid] + do_tb[do])
    return answer