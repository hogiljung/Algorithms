def solution(food):
    answer = []
    
    for i, count in enumerate(food[1:]):
        for _ in range(int(count)//2):
            answer.append(str(i+1))
        
    return ''.join(answer) + '0' + ''.join(answer[::-1])