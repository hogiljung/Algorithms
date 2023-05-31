import heapq

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    INF = int(1e9)
    distance = [INF] * (n+1)
    
    for v in edge:
        start, end = v
        graph[start].append([end, 1])
        graph[end].append([start, 1])
        
    q = []
    start = 1
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    
    while q:
        move, now = heapq.heappop(q)
        
        if distance[now] < move:
            continue
        
        for end, dist in graph[now]:
            cost = move + dist
            if cost < distance[end]:
                distance[end] = cost
                heapq.heappush(q, (cost, end))
                
    return distance[1:].count(max(distance[1:]))