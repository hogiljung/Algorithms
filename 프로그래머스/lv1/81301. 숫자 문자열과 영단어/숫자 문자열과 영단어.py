def solution(s):
    if s.isdigit():
        return int(s)
    
    answer = ''
    number_word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    tmp = ''
    
    for c in s:
        if c.isdigit():
            answer += str(c)
            continue
            
        tmp += c
        if tmp in number_word:
            answer += str(number_word.index(tmp))
            tmp = ''
            
    return int(answer)