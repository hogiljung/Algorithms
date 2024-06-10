def solution(clothes):
    answer = 0
    
    cloth_map = {}
    
    for cloth, cloth_type in clothes:
        if cloth_type not in cloth_map:
            cloth_map[cloth_type] = 1
        else:
            cloth_map[cloth_type] += 1
        
    for cloth_count in cloth_map.values():
        if answer == 0:
            answer = cloth_count + 1
        else:
            answer *= cloth_count + 1
            
    if answer > 0:
        answer -= 1
    
    return answer