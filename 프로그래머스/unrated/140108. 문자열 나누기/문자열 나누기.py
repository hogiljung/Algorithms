def solution(s):
    answer = 0
    x_count = 0
    other_count = 0

    for c in s:
        if x_count == other_count:
            x = c
            answer += 1
        
        if c != x:
            other_count += 1
        else:
            x_count += 1
    
    return answer