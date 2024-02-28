from collections import deque

oil_group_values = []
moves = [[1,0], [-1,0], [0, 1], [0,-1]]

def solution(land):
    answer = 0
    
    for x in range(len(land[0])):
        oil_set = set()
        for y in range(len(land)):
            if (oil_group:=land[y][x]) == 0:
                continue
            elif oil_group == 1:
                oil_group, value = bfs(land, x, y)
                oil_group_values.append(value)
            oil_set.add(oil_group)
        value = sum([oil_group_values[oil_group-2] for oil_group in oil_set])
        answer = max(answer, value)
        
    return answer

def bfs(land, x, y):
    oil_group = len(oil_group_values) + 2
    land[y][x] = oil_group
    
    value = 1

    q = deque([[x, y]])
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or nx >= len(land[0]) or ny < 0 or ny >= len(land):
                continue
            
            if land[ny][nx] == 1:
                land[ny][nx] = oil_group
                value += 1
                q.append([nx, ny])
    return oil_group, value