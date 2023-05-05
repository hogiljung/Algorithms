from collections import Counter

def solution(participant, completion):
    not_completed = Counter(participant) - Counter(completion)
    return list(not_completed)[0]