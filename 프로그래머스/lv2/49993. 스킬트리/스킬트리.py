def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        count = 0
        for s in skill_tree:
            if s in skill:
                if s != skill[count]:
                    break
                count += 1
        else:
            answer += 1

    return answer