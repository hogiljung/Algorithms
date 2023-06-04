"""
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = int(1e9)
    WORLD_SIZE = 100
    world = [[0 for _ in range(WORLD_SIZE+1)] for _ in range(WORLD_SIZE+1)]
    
    for lx, ly, rx, ry in map(double, rectangle):
        for x in range(lx, rx+1):
            world[ry][x] = 1
            world[ly][x] = 1
        for y in range(ly, ry+1):
            world[y][lx] = 1
            world[y][rx] = 1
    
    for lx, ly, rx, ry in map(double, rectangle):
        for x in range(lx+1, rx):
            for y in range(ly+1, ry):
                world[y][x] = 0
    
    def dfs(x, y, count):
        nonlocal answer
        if x<0 or x>=WORLD_SIZE or y<0 or y>=WORLD_SIZE:
            return False
        count += 1
        if x == itemX*2 and y == itemY*2:
            if count < answer:
                answer = count
            return True
        
        if world[y][x] == 1:
            world[y][x] = count
            dfs(x-1, y, count)
            dfs(x+1, y, count)
            dfs(x, y-1, count)
            dfs(x, y+1, count)
    
    dfs(characterX*2, characterY*2, -1)
    return answer//2

def double(numbers):
    for n in numbers:
        yield n*2
        
"""
from collections import deque

def solution(rectangle,cx,cy,ix,iy):
    candy = set()
    for x,y,X,Y in rectangle:
        candy.update([(j+0.5, i) for j in range(y, Y) for i in (x, X)])
        candy.update([(j,i+0.5) for i in range(x, X) for j in (y, Y)])

    edge = set()
    for b,a in candy:
        for x,y,X,Y in rectangle:
            if x<a<X and y<b<Y:
                break
        else:
            edge.add((b,a))

    que,dy,dx = deque([(0, cy, cx)]), [.5,0,-.5,0], [0,.5,0,-.5]
    while que:
        cnt,b,a = que.popleft()
        if a==ix and b==iy:
            return cnt
        for i in range(4):
            if ((is_in_edge_y:=b+dy[i]), (is_in_edge_x:=a+dx[i])) in edge:
                edge.remove((is_in_edge_y, is_in_edge_x))
                que.append((cnt+1, b+2*dy[i], a+2*dx[i]))