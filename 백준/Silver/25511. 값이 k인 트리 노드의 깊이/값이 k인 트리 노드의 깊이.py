import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())

    visited = [-1] * (n)
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)

    stack = [(0, 0)]
    while stack:
        (v, depth) = stack.pop()
        if visited[v] != -1:
            continue

        visited[v] = depth

        for connected_v in graph[v]:
            stack.append((connected_v, depth+1))

    values = list(map(int, input().split()))
    print(visited[values.index(k)])

solution()