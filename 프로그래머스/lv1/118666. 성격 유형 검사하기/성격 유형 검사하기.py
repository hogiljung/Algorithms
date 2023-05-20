def solution(survey, choices):
    answer = ''
    category = ['R','T','C','F','J','M','A','N']
    score = [0]*8
    
    for c, choice in zip(survey, choices):
        index = -1
        if choice < 4:
            index = category.index(c[0])
        elif choice > 4:
            index = category.index(c[1])
            
        if index != -1:
            score[index] += abs(4-choice)
            
    for i in range(4):
        if score[i*2] >= score[i*2+1]:
            answer += category[i*2]
        else:
            answer += category[i*2+1]
    return answer