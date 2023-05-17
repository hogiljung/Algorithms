def solution(lottos, win_nums):
    win = 0
    zero_count = 0
    for lotto in lottos:
        if lotto in win_nums:
            win += 1
        elif lotto == 0:
            zero_count += 1
            
    rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    
    return [rank[win+zero_count], rank[win]]