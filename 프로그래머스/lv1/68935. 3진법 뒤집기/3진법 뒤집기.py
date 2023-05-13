def solution(n):
    answer = 0
    third_count = ''
    while n > 0:
        third_count += str(n % 3)
        n //= 3
    
    for i, c in enumerate(third_count):
        answer += (3**(len(third_count)-1 - i)) * int(c)
    return answer