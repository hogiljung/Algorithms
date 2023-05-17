def solution(number, limit, power):
    answer = 0
    divisor_counts = [1] + [2] * (number-1)
    
    for i in range(2, number+1):
        tmp = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                divisor_counts[i-1] += 2
        if int(i**0.5) == i**0.5:
            divisor_counts[i-1] -= 1
            
    for divisor_count in divisor_counts:
        if divisor_count > limit:
            answer += power
        else:
            answer += divisor_count
    
    return answer

