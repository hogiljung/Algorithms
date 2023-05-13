def solution(n):
    answer = 0
    third_count = ''
    while n > 0:
        third_count += str(n % 3)
        n //= 3
    
    answer = int(third_count, 3)
    return answer