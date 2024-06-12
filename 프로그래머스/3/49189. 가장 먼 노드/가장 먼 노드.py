from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    visited = [False] * (n+1)
    
    start = 1
    visited[start] = True
    q = deque([1])
    
    while q:
        answer = len(q)

        for _ in range(len(q)):
            node = q.popleft()
            for connected in graph[node]:
                if not visited[connected]:
                    visited[connected] = True
                    q.append(connected)

    return answer