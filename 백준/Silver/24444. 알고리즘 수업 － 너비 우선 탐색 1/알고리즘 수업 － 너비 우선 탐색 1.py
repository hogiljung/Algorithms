import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for connected in graph:
        connected.sort()
    
    visited = [0] * (N+1)
    order = 1
    queue = deque()
    queue.append(R)
    while queue:
        v = queue.popleft()
        if visited[v]:
            continue

        visited[v] = order
        order += 1
        for connected in graph[v]:
            if not visited[connected]:
                queue.append(connected)

    print(*visited[1:], sep="\n")

solution()