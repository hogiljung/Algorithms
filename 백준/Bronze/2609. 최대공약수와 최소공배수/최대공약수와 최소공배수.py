x, y = map(int, input().split())

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

g = gcd(x, y)
print(g)
print(x*y//g)