import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
grpah = [[] for _ in range(N + 1)]

M = int(input())

for _ in range(M):
    start, end = map(int, input().split())
    grpah[start].append(end)
    grpah[end].append(start)

visited = [False] * (N + 1)


def bfs(grpah, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in grpah[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(grpah, 1, visited)

print(visited.count(True) - 1)
