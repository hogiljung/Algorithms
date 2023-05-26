from collections import Counter
def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    for c in count:
        k -= c[1]
        answer += 1
        if k <= 0:
            break
    
    return answer