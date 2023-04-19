def solution(arr):
    answer = []
    
    for n in arr:
        if answer:
            last = answer.pop()
            if last != n:
                answer.append(last)
        answer.append(n)
        
    return answer