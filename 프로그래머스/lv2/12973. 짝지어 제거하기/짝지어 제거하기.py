def solution(s):
    answer = -1
    temp = []
    
    for c in s:
        if temp and temp[-1] == c:
            temp.pop()
        else:
            temp.append(c)
    
    if temp:
        return 0
    else:
        return 1