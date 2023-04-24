def solution(spell, dic):
    answer = 2
    
    for word in dic:
        know = True
        for s in spell:
            if s not in word:
                know = False
                break
            
        if know:
            answer = 1
            break
            
    return answer