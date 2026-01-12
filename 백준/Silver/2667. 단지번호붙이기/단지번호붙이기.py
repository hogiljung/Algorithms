import sys

input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def dfs(graph, x, y, check):
    if not (0 <= y < N and 0 <= x < N) or graph[y][x] == 0 or graph[y][x] == check:
        return

    graph[y][x] = check
    dfs(graph, x, y + 1, check)
    dfs(graph, x + 1, y, check)
    dfs(graph, x, y - 1, check)
    dfs(graph, x - 1, y, check)


N = int(input())

graph = []

for _ in range(N):
    s = input().strip()
    graph.append(list(map(int, s)))

check = 2
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            dfs(graph, x, y, check)
            check += 1

cnt_list = []

for c in range(check - 1, 1, -1):
    cnt = 0
    for g in graph:
        cnt += g.count(c)
    cnt_list.append(cnt)

print(len(cnt_list))
for cnt in sorted(cnt_list):
    print(cnt)
