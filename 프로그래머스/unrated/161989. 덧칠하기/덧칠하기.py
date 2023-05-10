def solution(n, m, section):
    answer = 1
    prev = section[0]
    
    for now in section:
        if now - prev >= m:
            prev = now
            answer += 1
        
    return answer