def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = gcd(numer, denom)
    return [numer // g, denom // g]

def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    
    return x