import re

def solution(babbling):
    answer = 0
    regex = r"^(aya|ye|ma|woo)+$"
    for i in babbling:
        if re.match(regex, i):
            answer += 1
            
    return answer