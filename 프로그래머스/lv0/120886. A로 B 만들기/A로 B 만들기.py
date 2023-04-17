def solution(before, after):
    for c in before:
        if before.count(c) != after.count(c):
            return 0
    return 1