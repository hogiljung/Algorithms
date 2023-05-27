def solution(elements):
    temp = set()
    for _ in range(len(elements)):
        for i in range(1, len(elements)+1):
            temp.add(sum(elements[:i]))
        elements = elements[1:] + [elements[0]]
    return len(temp)