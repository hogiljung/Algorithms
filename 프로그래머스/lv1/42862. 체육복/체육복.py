def solution(n, lost, reserve):
    l_list = sorted(list(set(lost) - set(reserve)))
    r_list = sorted(list(set(reserve) - set(lost)))
    
    for r in r_list:
        if r-1 in l_list:
            l_list.remove(r-1)
        elif r+1 in l_list:
            l_list.remove(r+1)
    
    return n - len(l_list)