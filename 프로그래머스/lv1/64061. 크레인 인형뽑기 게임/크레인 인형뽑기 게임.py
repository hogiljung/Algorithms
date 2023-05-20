def solution(board, moves):
    answer = 0
    bag = []
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                if len(bag)>0 and bag[-1] == board[i][m-1]:
                    bag.pop()
                    answer += 2
                else:
                    bag.append(board[i][m-1])
                board[i][m-1] = 0
                break
        
    return answer