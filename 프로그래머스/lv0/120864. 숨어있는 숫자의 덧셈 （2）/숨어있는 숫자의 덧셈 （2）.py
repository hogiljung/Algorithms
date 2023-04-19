def solution(my_string):
    s = ''.join(c if c.isdigit() else ' ' for c in my_string)
    return sum(int(c) for c in s.split())