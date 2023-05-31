def solution(n, k):
    answer = 0
    k_n = ''
    
    while n:
        k_n += str(n%k)
        n //= k
    k_n = k_n[::-1]
    
    for num in k_n.split('0'):
        if num and isPrime(int(num)):
            answer += 1
            
    return answer

def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
    return True
        