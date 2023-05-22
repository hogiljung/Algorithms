def solution(s):
    answer = [0]*2
    if '1' not in s:
        answer[1] += s.count('0')
        return answer
    
    while len(s)>1:
        answer[1] += s.count('0')
        answer[0] += 1
        s = str(bin(s.count('1')))[2:]
    
    return answer