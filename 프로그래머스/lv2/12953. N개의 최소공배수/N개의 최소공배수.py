def solution(arr):
    answer = arr.pop()
    
    while len(arr) > 0:
        x = arr.pop()
        g = gcd(answer, x)
        
        answer = answer*x//g
    
    return answer

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x