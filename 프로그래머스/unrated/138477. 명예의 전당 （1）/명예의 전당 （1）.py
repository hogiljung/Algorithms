def solution(k, score):
    answer = []
    glory = []
    
    for s in score:
        glory.append(s)
        glory.sort(reverse=True)
        if len(glory) > k:
            glory.pop()
        answer.append(glory[len(glory)-1])
        
    return answer