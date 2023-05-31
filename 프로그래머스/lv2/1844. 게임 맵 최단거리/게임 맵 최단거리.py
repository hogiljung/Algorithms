from collections import deque

def solution(maps):
    answer = -1
    MAPS_ROWS = len(maps[0])
    MAPS_COLS = len(maps)
    mv = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q = deque([(0,0)])
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in mv:
            nx = x + dx
            ny = y + dy
            
            if nx<0 or nx>=MAPS_ROWS or ny<0 or ny>=MAPS_COLS or maps[ny][nx] == 0:
                continue
            
            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x]+1
                q.append((nx, ny))

    if maps[MAPS_COLS-1][MAPS_ROWS-1] != 1:
        answer = maps[MAPS_COLS-1][MAPS_ROWS-1]
    
    return answer