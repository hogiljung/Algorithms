def solution(array):
    return sum(str(c).count('7') for c in array)