def solution(name):
    answer = 0
    need_to_change = []
    # 모든 문자열을 확인할 때까지 아래를 반복한다.
    
    start = 0
    move = 0
    
    
    
    
    for i in range(len(name)):
        
    # 양쪽으로 이동하며 변경해야 하는 문자를 찾는다.
    # 그 때까지의 거리를 더한다.
    # 위, 아래로의 이동 횟수도 구하여 더한다.
    
    
    # 문자열을 순회하여
    # 위로 이동하는게 빠른지 아래로 이동하는게 빠른지를 이용해
    # 각 원소당 이동 횟수를 구할 수 있고,
    for c, i in enumerate(name):
        if c == 'A':    
            continue
            
        min_up_or_down_move = min(\
            ord('A') - ord(c),
            ord('Z') - ord(c) + 1
        )
        answer += min_up_or_down_move
        
        min_left_or_right_move = 
        
        need_to_change.append((i))
            
    
    # 변경해야 하는 원소의 위치와 이동에 필요한 값을 기록한다.
    
    # 현재 가장 가까운 변경해야 하는 원소로 이동하는 값을 더한다.
    
    
    return answer