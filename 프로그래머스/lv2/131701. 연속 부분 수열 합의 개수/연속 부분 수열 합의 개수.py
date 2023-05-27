from collections import deque
def solution(elements):
    temp = set()
    elements = deque(elements)
    for _ in range(len(elements)):
        s = 0
        for i in range(len(elements)):
            s += elements[i]
            temp.add(s)
        elements.append(elements.popleft())
    return len(temp)