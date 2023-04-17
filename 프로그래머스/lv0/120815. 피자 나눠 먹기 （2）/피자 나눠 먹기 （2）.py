def solution(n):
    return n//gcd(n,6)

def gcd(x,y):
    while y:
        x,y = y,x%y
    return x