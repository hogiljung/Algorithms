from collections import deque

def solution(n, computers):
    global visited
    answer = 0
    N = len(computers)
    for i in range(N):
        if computers[i][i] == 1:
            bfs(i, computers)
            answer += 1
    return answer

def bfs(start, computers):
    q = deque()
    q.append(start)

    while q:
        start = q.popleft()
        computers[start][start] = 0
        for end in range(len(computers[start])):
            if computers[start][end] == 1:
                computers[start][end] = 0
                q.append(end)
    