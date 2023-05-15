def solution(s):
    answer = ''
    number_word_tb = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    i = 0
    
    while i < len(s):
        if s[i].isdigit():
            answer += str(s[i])
            i += 1
            continue
        
        j = 3
        while s[i:i+j] not in number_word_tb:
            j += 1
            
        answer += number_word_tb[s[i:i+j]]
        i += j
        
    return int(answer)