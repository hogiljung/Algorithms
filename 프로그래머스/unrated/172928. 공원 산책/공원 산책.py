def solution(park, routes):
    location = [0,0]
    direction = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}

    for y, row in enumerate(park):
        for x, col in enumerate(row):
            if col == 'S':
                location = [y,x]
                break

    for route in routes:
        d, l = route.split()
        ny, nx = location
        for _ in range(int(l)):
            nx += direction[d][1]
            ny += direction[d][0]
            if nx>=len(park[0]) or nx<0 or ny>=len(park) or ny<0  or park[ny][nx] == 'X':
                ny, nx = location
                break
        location = [ny, nx]
            
    return location