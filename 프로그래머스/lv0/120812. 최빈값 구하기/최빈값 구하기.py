from collections import Counter

def solution(array):
    cnt = Counter(array).most_common(2)
    if len(cnt) == 1:
        return cnt[0][0]
    return -1 if cnt[0][1] == cnt[1][1] else cnt[0][0]
