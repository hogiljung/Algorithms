visited = []
N = 0
answer = -1

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [False] * N
    dfs(k, 0, dungeons)
    return answer

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    
    for i in range(N):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            visited[i] = False










