def solution(clothes):
    answer = 1
    clothes_tb = {}
    
    for cloth_name, cloth_type in clothes:
        clothes_tb.setdefault(cloth_type, [])
        clothes_tb[cloth_type].append(cloth_name)
    
    for cloth_type in clothes_tb.keys():
        answer *= len(clothes_tb[cloth_type])+1
    
    return answer-1