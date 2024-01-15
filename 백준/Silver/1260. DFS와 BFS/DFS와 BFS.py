from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, visited, start):
    s = [start]

    while s:
        v = s.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')

            for connected_v in graph[v]:
                if not visited[connected_v]:
                    s.append(connected_v)

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for connected_v in graph[v]:
            if not visited[connected_v]:
                queue.append(connected_v)
                visited[connected_v] = True

def solution():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N+1):
        graph[i].sort(reverse=True)

    visited = [False] * (N+1)

    dfs(graph, visited.copy(), V)
    print()

    for i in range(1, N+1):
        graph[i].sort()

    bfs(graph, visited.copy(), V)

if __name__ == '__main__':
    solution()