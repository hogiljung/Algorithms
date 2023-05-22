def solution(brown, yellow):
    answer = []
    
    for i in range(1, (brown+yellow)+1):
        if yellow % i == 0:
            divisor, q = i, yellow//i
            if 2*((divisor+2) + (q+2)) - 4 == brown:
                answer = [max(divisor, q)+2, min(divisor, q)+2]
                break
                
    return answer