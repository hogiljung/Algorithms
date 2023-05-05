def solution(participant, completion):
    answer = ''
    p_tb = {}
    
    for p in participant:
        p_tb.setdefault(p, 0)
        p_tb[p] += 1
    
    for c in completion:
        p_tb[c] -= 1
        
    for k, v in p_tb.items():
        if v == 1:
            answer = k
            
    return answer