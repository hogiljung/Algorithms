def solution(my_string):
    gathers = 'aeiou'
    return ''.join(c for c in my_string if c not in gathers)