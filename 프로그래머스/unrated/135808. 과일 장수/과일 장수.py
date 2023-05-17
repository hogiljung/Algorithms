def solution(k, m, score):
    answer = 0
    score_sorted = sorted(score, reverse=True)
    
    for i in range(m-1, len(score_sorted), m):
        answer += score_sorted[i]*m
        
    return answer