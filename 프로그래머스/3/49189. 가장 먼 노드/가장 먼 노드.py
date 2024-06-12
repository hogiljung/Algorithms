from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    visited = [-1] * (n+1)
    
    dist = 0
    visited[1] = dist
    q = deque([1])
    
    while q:
        dist += 1

        for _ in range(len(q)):
            node = q.popleft()
            for connected in graph[node]:
                if visited[connected] == -1:
                    visited[connected] = dist
                    q.append(connected)

    return visited.count(dist-1)