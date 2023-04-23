def solution(answers):
    solves = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    
    answers_count = [0] * len(solves)
    
    for i in range(3):
        for j, answer in enumerate(answers):
            if solves[i][j % len(solves[i])] == answer: 
                answers_count[i] += 1
    
    best = []
    for i in range(3):
        if max(answers_count) == answers_count[i]:
            best.append(i+1)
        
    return best