def solution(players, callings):
    rank_tb = {v:i for i,v in enumerate(players)}
    
    for calling in callings:
        up, down = rank_tb[calling]-1, rank_tb[calling]
        rank_tb[players[up]] = down
        rank_tb[players[down]] = up
        players[up], players[down] = players[down], players[up]
    return players