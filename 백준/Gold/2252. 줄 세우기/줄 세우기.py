from collections import deque
import sys
input = sys.stdin.readline


def topology_sort(graph, indgree: list[int]):
    result = []
    q = deque()

    for i in range(1, len(indgree)):
        if indgree[i] == 0:
            q.append(i)
    
    for i in range(1, len(indgree)):
        x = q.popleft()
        result.append(x)

        for v in graph[x]:
            indgree[v] -= 1

            if indgree[v] == 0:
                q.append(v)
    
    print(*result)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    indgree = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indgree[b] += 1
    topology_sort(graph, indgree)
