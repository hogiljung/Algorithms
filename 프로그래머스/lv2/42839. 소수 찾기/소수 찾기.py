numbers_combinations = set()

def solution(numbers):
    makeCombinations("", numbers)
    
    answer = len(numbers_combinations)
    
    return answer

def makeCombinations(str1, str2):
    print(str1)
    if str1 != "" and isPrime(int(str1)):
        numbers_combinations.add(int(str1))
        
    for i in range(len(str2)):
        makeCombinations(str1+str2[i], str2[:i]+str2[i+1:])
        
def isPrime(n):
    if n in (0, 1):
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True