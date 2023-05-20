def solution(survey, choices):
    answer = ''
    category = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    
    for s, choice in zip(survey, choices):
        if s not in category:
            s = s[::-1]
            category[s] -= 4-choice
        else:
            category[s] += 4-choice
    
    for k, v in category.items():
        if v > 0:
            answer += k[0]
        elif v < 0:
            answer += k[1]
        else:
            answer += sorted(k)[0]
    return answer