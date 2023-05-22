def solution(n):
    answer = n+1
    count = str(bin(n))[2:].count('1')
    
    while count != str(bin(answer))[2:].count('1'):
        answer += 1
        
    return answer