def solution(money):
    price = 5500
    num = money//price
    return [num, money-price*num]