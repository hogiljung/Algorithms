def solution(n, m):
    g = gcd(n, m)
    l = n*m//g
    return [g, l]

def gcd(n, m):
    while m:
        n, m = m, n%m
    return n