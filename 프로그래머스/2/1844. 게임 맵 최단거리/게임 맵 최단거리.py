from collections import deque

def solution(maps):    
    d = [[1,0], [-1,0], [0,1], [0,-1]]
    
    q = deque([[0, 0]])
    
    while q:
        x, y = q.popleft()
        move = maps[y][x]

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= len(maps[0])\
                or ny < 0 or ny >= len(maps): 
                continue
            
            if maps[ny][nx] == 1:
                maps[ny][nx] = move + 1
                q.append([nx, ny])

    return maps[-1][-1] if maps[-1][-1] != 1 else -1