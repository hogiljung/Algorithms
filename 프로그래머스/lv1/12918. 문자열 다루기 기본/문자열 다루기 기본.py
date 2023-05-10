def solution(s):
    if len(s) not in (4, 6):
        return False
    
    for c in s:
        if not c.isdigit():
            return False
    return True