def solution(s):
    answer = []
    tb = {}
    
    for i, c in enumerate(s):
        if c not in tb:
            answer.append(-1)
        else:
            answer.append(i-tb[c])
        
        tb[c] = i
    return answer