def solution(dots):
    width = 0
    height = 0
    for dot in dots[1:]:
        if dots[0][0] != dot[0] and dots[0][1] != dot[1]:
            width = abs(dots[0][0] - dot[0])
            height = abs(dots[0][1] - dot[1])
            break
    
    return width * height