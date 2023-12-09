import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

visited = [-1] * (N+1)
graph = [[] for _ in range(N+1)]
stack = []

def dfs(x):
    stack.append((x, 0))
    while stack:
        (v, depth) = stack.pop()
        if visited[v] != -1:
            continue

        visited[v] = depth

        for connected_v in graph[v]:
            stack.append((connected_v, depth+1))

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for connecion in graph:
    connecion.sort()

dfs(R)

print(*visited[1:], sep="\n")