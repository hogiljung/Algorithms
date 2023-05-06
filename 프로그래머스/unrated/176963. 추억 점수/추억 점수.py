def solution(name, yearning, photo):
    answer = [0] * len(photo)
    point = {k:v for k,v in zip(name, yearning)}
    
    for i, people in enumerate(photo):
        for person in people:
            if person in point:
                answer[i] += point[person]
    
    return answer