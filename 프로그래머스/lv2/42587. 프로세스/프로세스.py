from collections import deque

def solution(priorities, location):
    completed = 0
    priorities_tb = sorted(priorities, reverse=True)
    q = deque([(p, i) for i, p in enumerate(priorities)])
    
    while q:
        p = q.popleft()

        if p[0] == priorities_tb[completed]:
            completed += 1

            if p[1] == location:
                break
        else:
            q.append(p)

    return completed