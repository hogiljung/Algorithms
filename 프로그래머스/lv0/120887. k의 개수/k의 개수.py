def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        while n > 0:
            if n % 10 == k:
                answer += 1
            n //= 10
    return answer