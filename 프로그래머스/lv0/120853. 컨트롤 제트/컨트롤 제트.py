def solution(s):
    s_list = [c for c in s.split()]

    for i, c in enumerate(s_list):
        if c == 'Z':
            s_list[i-1] = s_list[i] = 0

    return sum(map(int, s_list))