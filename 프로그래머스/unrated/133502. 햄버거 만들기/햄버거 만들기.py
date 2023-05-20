def solution(ingredient):
    answer = 0
    hamburger = []
    
    for i in ingredient:
        hamburger.append(i)
        if hamburger[-4:] == [1, 2, 3, 1]:
            for i in range(4):
                hamburger.pop()
            answer += 1
    
    return answer