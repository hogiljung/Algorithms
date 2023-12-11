from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def solution():
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    start = int(input())
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    INF = 10e9
    distances = [INF] * (V+1)

    distances = dijkstra(graph, distances, start)

    for distance in distances[1:]:
        print(distance) if distance != INF else print("INF")

def dijkstra(graph, distances, start):
    distances[start] = 0
    q = []
    heappush(q, (distances[start], start))

    while q:
        distance_now, now = heappop(q)

        if distances[now] < distance_now:
            continue

        for end, distance_end in graph[now]:
            distance_diesel = distance_now + distance_end
            if distance_diesel < distances[end]:
                distances[end] = distance_diesel
                heappush(q, (distance_diesel, end))

    return distances

if __name__=='__main__':
    solution()