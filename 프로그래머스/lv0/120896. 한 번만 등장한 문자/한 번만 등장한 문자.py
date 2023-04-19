def solution(s):
    s_list = [c for c in s]
    for c in set(s):
        s_list.remove(c)
        
    return ''.join(sorted([c for c in s if c not in s_list]))