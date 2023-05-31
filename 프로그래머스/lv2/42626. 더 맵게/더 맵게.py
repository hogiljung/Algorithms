import heapq

def solution(scoville, K):
    answer = 0
    q = []
    
    for s in scoville:
        heapq.heappush(q, s)
    
    if q[-1] == 0:
        return -1
    
    while q[0] < K:
        if len(q) == 1:
            answer = -1
            break
        
        s1 = heapq.heappop(q)
        s2 = heapq.heappop(q)
        heapq.heappush(q, s1+s2*2)
        answer += 1
        
    return answer