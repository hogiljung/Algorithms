def solution(keymap, targets):
    answer = []
    key_dict = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in key_dict or key_dict[key] > i+1:
                key_dict[key] = i+1
                
    for target in targets:
        count = 0
        for c in target:
            if c not in key_dict:
                count = -1
                break
            
            count += key_dict[c]
        answer.append(count)
    
    return answer