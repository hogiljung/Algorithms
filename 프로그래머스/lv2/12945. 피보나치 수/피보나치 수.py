def solution(n):
    answer = 0
    fibo = {0:0, 1:1}
    
    for i in range(2, n+1):
        fibo[i] = fibo[i-2] + fibo[i-1]
    
    return fibo[n] % 1234567