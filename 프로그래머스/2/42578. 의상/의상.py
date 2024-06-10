from collections import Counter
from functools import reduce

def solution(clothes):
    cnt_map = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt_map.values(), 1) - 1
    return answer