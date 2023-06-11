def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        can = True
        learned = [False] * len(skill)
        for s in skill_tree:
            if s in skill:
                i = skill.index(s)
                learned[i] = True
                if not all(learned[:i]):
                    can = False
                    break
        if can:
            answer += 1
    
    return answer