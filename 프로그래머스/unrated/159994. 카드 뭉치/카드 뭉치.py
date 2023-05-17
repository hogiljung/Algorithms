def solution(cards1, cards2, goal):
    seperated_goal = [[],[]]
    
    for word in goal:
        if word in cards1:
            seperated_goal[0].append(word)
        else:
            seperated_goal[1].append(word)
            
    return 'Yes' if ''.join(seperated_goal[0]) in ''.join(cards1) and ''.join(seperated_goal[1]) in ''.join(cards2) else 'No'