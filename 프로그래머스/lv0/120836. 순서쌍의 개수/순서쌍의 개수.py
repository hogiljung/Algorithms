def solution(n):
    answer = sum(1 for i in range(1, int(n**0.5)+1) if n%i == 0) * 2
    return answer-1 if n%(n**0.5) == 0 else answer