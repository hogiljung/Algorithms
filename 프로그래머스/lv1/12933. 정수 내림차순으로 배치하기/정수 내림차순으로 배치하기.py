def solution(n):
    return int(''.join(c for c in sorted(str(n), reverse=True)))