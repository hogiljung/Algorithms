def solution(s):
    answer = ''
    for word in s.split(" "):
        tmp = ''
        for i, c in enumerate(word):
            if i % 2 == 0:
                tmp += c.upper()
            else:
                tmp += c.lower()
        answer += tmp + ' '
    return answer[:-1]