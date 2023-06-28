m = int(input())
n = int(input())

def isPrime(x):
    if x < 2:
        return False
    
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            return False
    return True

min_prime = -1
sum_primes = 0
for num in range(m, n+1):
    if isPrime(num):
        if min_prime == -1:
            min_prime = num
        sum_primes += num

if min_prime != -1:
    print(sum_primes)
print(min_prime)