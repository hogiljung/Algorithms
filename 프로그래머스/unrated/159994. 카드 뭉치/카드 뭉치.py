def solution(cards1, cards2, goal):
    seperated_goal = [[],[]]

    for word in goal:
        if word in cards1:
            seperated_goal[0].append(word)
        else:
            seperated_goal[1].append(word)

    return 'Yes' if seperated_goal[0] == cards1[:len(seperated_goal[0])] and seperated_goal[1] == cards2[:len(seperated_goal[1])] else 'No'