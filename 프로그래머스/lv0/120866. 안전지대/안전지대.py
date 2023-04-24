def solution(board):
    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    
    w, h = len(board[0]), len(board)
    
    for x in range(w):
        for y in range(h):
            if board[x][y] == 1:
                for i in range(len(dx)):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx<0 or nx>=w or ny<0 or ny>=h:
                        continue
                    
                    if board[nx][ny] != 1:
                        board[nx][ny] = 2

    answer = 0
    
    for line in board:
        answer += line.count(0)
    
    return answer