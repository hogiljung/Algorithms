def solution(s):
    answer = True
    check = []
    
    for c in s:
        if c == '(':
            check.append(c)
        elif c == ')':
            if len(check) == 0 or check[-1] != '(':
                return False
            check.pop()
    
    if len(check) > 0:
        return False    
    return True