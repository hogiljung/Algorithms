def solution(keyinput, board):
    answer = [0,0]
    move = {"up": [0,1], "down": [0,-1], "left": [-1,0], "right": [1,0]}
    max_x, max_y = board[0]//2, board[1]//2
    
    for key_input in keyinput:
        nx = answer[0] + move[key_input][0]
        ny = answer[1] + move[key_input][1]
        
        if abs(nx) > max_x or abs(ny) > max_y:
            continue
        
        answer[0], answer[1] = nx, ny
    
    return answer