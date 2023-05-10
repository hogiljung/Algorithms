def solution(n):
    answer = ''
    for c in sorted(str(n), reverse=True):
        answer += c
    return int(answer)