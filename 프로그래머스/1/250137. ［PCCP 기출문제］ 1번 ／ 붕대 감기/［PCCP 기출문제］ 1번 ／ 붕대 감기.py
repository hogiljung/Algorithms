def solution(bandage, health, attacks):
    answer = 0
    
    attack_index = 0
    current_health = health
    continued_success = 0
    
    for i in range(1, 1001):
        if attacks[attack_index][0] == i: 
            current_health -= attacks[attack_index][1]
            
            if current_health <= 0:
                answer = -1
                break
            
            attack_index += 1
            
            if attack_index == len(attacks):
                answer = current_health
                break
            
            continued_success = 0
            
            continue
                
        temp_health = current_health + bandage[1]
        continued_success += 1

        if continued_success == bandage[0]:
            temp_health += bandage[2]
            continued_success = 0
        
        current_health = min(temp_health, health)
        
    return answer