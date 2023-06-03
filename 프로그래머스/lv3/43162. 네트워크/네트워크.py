def solution(n, computers):
    answer = 0
    
    for i in range(len(computers)):
        if dfs(i, computers):
            answer += 1
    
    return answer

def dfs(v, computers):
    if computers[v][v] == 0:
        return False
    
    computers[v][v] = 0
    for i in range(len(computers)):
        if computers[v][i] == 1:
            computers[v][i] = 0
            dfs(i, computers)
    return True
    