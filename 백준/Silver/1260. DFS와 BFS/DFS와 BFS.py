import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
grpah = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().split())
    grpah[start].append(end)
    grpah[start].sort()
    grpah[end].append(start)
    grpah[end].sort()


visited = [False] * (N + 1)


def dfs(grpah, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in grpah[start]:
        if not visited[i]:
            dfs(grpah, i, visited)


dfs(grpah, V, visited)
print()


visited = [False] * (N + 1)


def bfs(grpah, start, visited):
    queue = deque([start])
    visited[start] = True
    print(start, end=" ")

    while queue:
        v = queue.popleft()
        for i in grpah[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=" ")


bfs(grpah, V, visited)
