def solution(spell, dic):
    answer = 2
    
    for word in dic:
        know = condition = True
        word_list = list(word)
        word_set = set(word)
        for spelling in word_set:
            word_list.remove(spelling)

        for spelling in word_list:
            if spelling in word_set:
                condition = False
                break
                
        if not condition:
            continue
        
        for s in spell:
            if s not in word_set:
                know = False
                break
            
        if know:
            answer = 1
            break
            
    return answer