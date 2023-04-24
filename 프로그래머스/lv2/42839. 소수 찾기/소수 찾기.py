from itertools import permutations

def solution(numbers):
    answer = 0
    numbers_list = [n for n in numbers]
    numbers_permutations = []
    for i in range(1, len(numbers_list)+1):
        for permutation in permutations(numbers_list, i):
            numbers_permutations.append(int(''.join(n for n in permutation)))
            
    for number in set(numbers_permutations):
        if isPrime(number):
            answer += 1
    return answer

def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True