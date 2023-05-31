def solution(msg):
    answer = []
    dictionary = {}
    
    for c in range(65, 91):
        dictionary[chr(c)] = c-64

    while msg not in dictionary:
        for i in range(1, len(msg)+1):
            if msg[:i] not in dictionary:
                answer.append(dictionary[msg[:i-1]])
                dictionary[msg[:i]] = len(dictionary)+1
                msg = msg[i-1:]
                break
    answer.append(dictionary[msg])
                
    return answer