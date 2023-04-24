def solution(dots):
    answer = 0
    
    for i in range(3):
        if getGradient(dots[-1], dots[i]) == getGradient(dots[(i+1)%3], dots[(i+2)%3]):
            answer = 1
            break
    return answer

def getGradient(dot1, dot2):
    return (dot2[1]-dot1[1]) / (dot2[0]-dot1[0])