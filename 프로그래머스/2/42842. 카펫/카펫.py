def solution(brown, yellow):
    answer = []
    
    for i in range(3, int((brown + yellow) ** .5) + 1):
        if (brown + yellow) % i == 0:
            r, c = i, (brown + yellow) // i
            if (r - 2) * (c - 2) == yellow:
                answer = [max(r, c), min(r, c)]
                break
                
    return answer