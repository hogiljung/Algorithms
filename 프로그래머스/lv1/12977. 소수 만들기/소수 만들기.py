from itertools import combinations

def solution(nums):
    answer = 0
    
    for combination in combinations(nums, 3):
        if isPrime(sum(combination)):
            answer += 1
            
    return answer

def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
