def solution(s):
    answer = []
    s = sorted(s[2:-2].split('},{'), key=lambda x: len(x))
    for tup in s:
        new = set(map(int, tup.split(','))) - set(answer)
        answer += list(new)
    return list(answer)