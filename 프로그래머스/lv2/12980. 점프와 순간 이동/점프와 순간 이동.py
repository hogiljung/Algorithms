def solution(n):
    ans = 0
    
    while n > 0:
        k = n % 2
        if k == 0:
            n //= 2
        else:
            n -= k
            ans += k
    
    return ans