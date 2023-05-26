from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    tangerine.sort(key = lambda t: (-counter[t], t))
    return len(set(tangerine[:k]))
