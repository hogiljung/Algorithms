def solution(s, skip, index):
    answer = ''
    code = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    code = [c for c in code if c not in skip]
    for c in s:
        answer += code[(code.index(c) + index) % len(code)]
    return answer