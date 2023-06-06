def solution(dirs):
    answer = 0
    moves = {'U':[0,1], 'D':[0,-1], 'R':[1,0], 'L':[-1,0]}
    curr_pos = [0, 0]
    path = []
    for d in dirs:
        next_pos = [c+m for c, m in zip(curr_pos, moves[d])]
        if next_pos[0] < -5 or next_pos[0] > 5 or next_pos[1] < -5 or next_pos[1] > 5:  continue
        if (curr_pos, next_pos) not in path and (next_pos, curr_pos) not in path:
            answer += 1
            path.append((curr_pos, next_pos))
        curr_pos = next_pos
        
    return answer