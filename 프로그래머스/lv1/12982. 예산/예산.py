def solution(d, budget):
    answer = 0
    d_sorted = sorted(d)
    
    for request in d_sorted:
        budget -= request
        if budget >= 0:
            answer += 1
        else:
            break
    
    return answer