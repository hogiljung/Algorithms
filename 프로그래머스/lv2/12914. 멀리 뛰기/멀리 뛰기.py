def solution(n):
    tb = [0] * 2001
    tb[1] = 1
    tb[2] = 2
    
    for i in range(3, n+1):
        tb[i] = tb[i-1] + tb[i-2]
    
    return tb[n] % 1234567