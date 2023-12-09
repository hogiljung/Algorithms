import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
visited_order = 0
stack = []

def dfs(x):
    global visited_order

    visited[x] = visited_order

    for v in sorted(graph[x]):
        if not visited[v]:
            visited_order += 1
            dfs(v)

def dfs2(x):
    global visited_order

    stack.append(x)
    while stack:
        v = stack.pop()
        if visited[v]:
            continue

        visited_order += 1
        visited[v] = visited_order

        stack.extend(graph[v])

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for connecion in graph:
    connecion.sort(reverse=True)

dfs2(R)

print(*visited[1:], sep="\n")