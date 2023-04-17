def solution(age):
    return ''.join(chr(ord('a')+int(x)) for x in str(age))
        