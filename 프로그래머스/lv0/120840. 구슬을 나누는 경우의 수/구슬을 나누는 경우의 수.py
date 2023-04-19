def solution(balls, share):
    return combination(balls, share)

def combination(n, r):
    return factorial(n)//factorial(r)//factorial(n-r)
    
def factorial(x):
    if x<=0:
        return 1
    return x * factorial(x-1)