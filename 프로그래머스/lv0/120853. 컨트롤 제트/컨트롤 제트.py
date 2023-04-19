def solution(s):
    s_stack = []

    for c in s.split():
        if c == 'Z':
            s_stack.pop()
        else:
            s_stack.append(int(c))

    return sum(s_stack)