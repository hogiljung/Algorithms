from math import gcd

def solution(a, b):
    return 1 if isFiniteDecimal(b//gcd(a,b)) else 2

def isFiniteDecimal(n):
    while n > 1:
        for i in range(2, n+1):
            if n%i == 0:
                if i!=2 and i!=5:
                    return False
                n //= i
                break
    return True
        
