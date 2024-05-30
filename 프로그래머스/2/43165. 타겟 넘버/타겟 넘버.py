from itertools import product

def solution(numbers, target):
    # +number,-number 로 이루어진 튜플의 배열을 만든다.
    l = [(number, -number) for number in numbers]
    # 튜플에서 하나씩 사용하여 만드는 모든 조합의 합의 배열을 만든다.
    s = list(map(sum, product(*l)))
    # target의 개수를 반환한다.
    return s.count(target)