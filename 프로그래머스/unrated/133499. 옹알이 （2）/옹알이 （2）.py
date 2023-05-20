import re

def solution(babbling):
    answer = 0
    speaks = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for speak in speaks:
            if speak*2 not in bab:
                bab = bab.replace(speak, ' ')
                
        if bab.strip() == '':
            answer += 1
    
    return answer