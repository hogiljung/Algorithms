def solution(order):
    return sum(1 for x in str(order) if x!='0' and int(x)%3==0)