def solution(a, b, n):
    answer = 0
    remain = n
    
    while remain >= a:
        bonus, remain = divmod(remain, a)
        bonus *= b
        remain += bonus
        answer += bonus
    return answer