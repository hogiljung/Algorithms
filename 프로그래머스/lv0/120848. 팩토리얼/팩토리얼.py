def solution(n):
    answer = 1
    for i in range(1, 11):
        answer *= (i+1)
        if answer > n:
            return i