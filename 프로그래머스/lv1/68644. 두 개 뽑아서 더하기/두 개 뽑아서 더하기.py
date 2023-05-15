from itertools import combinations

def solution(numbers):
    answer = []
    
    for c in combinations(numbers, 2):
        answer.append(sum(c))
    
    return sorted(set(answer))