def solution(sides):
    answer = 0
    for i in range(1, max(sides)+1):
        if isTriangleAvailable(sides, i):
            answer += 1
    
    for i in range(max(sides)+1, sum(sides)):
        if isTriangleAvailable(sides, i):
            answer += 1
    
    return answer

def isTriangleAvailable(sides, l):
    sides.append(l)
    result = max(sides) < sum(sides) - max(sides)
    sides.pop()
    return result