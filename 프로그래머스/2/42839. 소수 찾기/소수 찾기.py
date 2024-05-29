from itertools import permutations

def solution(numbers):
    answer = 0
    
    def is_prime(n):
        if n <= 1:
            return False
        
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                return False
        return True
    
    checked_number = set()
    
    for i in range(1, len(numbers) + 1):
        for p_arr in permutations(numbers, i):
            num = int(''.join(p_arr))
            
            if num in checked_number:
                continue
            
            checked_number.add(num)
                
            if is_prime(num):
                answer += 1
    
    return answer