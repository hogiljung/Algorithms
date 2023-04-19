def solution(my_string):
    answer_str = []
    prev = False
    for c in my_string:
        if c.isdigit():
            if not prev:
                answer_str.append(c)
                prev = True
            else:
                answer_str[len(answer_str)-1] += c
        else:
            prev = False
    return sum(int(n) for n in answer_str)