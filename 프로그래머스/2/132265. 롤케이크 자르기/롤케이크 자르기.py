def solution(topping):
    answer = 0
    
    if len(topping) == 1:
        return answer
    
    brother = {}
    for t in topping:
        if t in brother:
            brother[t] += 1
        else:
            brother[t] = 1

    cheolsu = set()
    
    for t in topping:
        cheolsu.add(t)
        if brother[t] > 1:
            brother[t] -= 1
        else:
            del brother[t]

        c_topping = len(cheolsu)
        b_topping = len(brother.keys())
        
        if c_topping > b_topping:
            break
        
        if c_topping == b_topping:
            answer += 1
        
    return answer