def solution(rsp):
    wins = {'5':'2', '2':'0', '0':'5'}
    return ''.join(wins[x] for x in rsp)