def solution(n):
    answer = 0
    for x in range(4, n+1):
        for y in range(2, int(x**0.5)+1):
            if x%y==0:
                answer += 1
                break
    return answer