def solution(x, n):
    if x == 0:
        return [x] * n
    return [i for i in range(x, x*(n+1), x)]