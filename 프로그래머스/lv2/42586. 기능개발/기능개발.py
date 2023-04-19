from collections import deque

def solution(progresses, speeds):
    answer = []
    p, s = deque(progresses), deque(speeds)
    
    while p:
        count = 0
        while p[0] < 100:
            for i in range(len(p)):
                p[i] += s[i]
        
        while p and p[0] >= 100:
            p.popleft()
            s.popleft()
            count += 1
            
        answer.append(count)

        
    return answer