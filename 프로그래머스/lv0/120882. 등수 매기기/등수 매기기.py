def solution(score):
    avgs = []
    for math_eng_score in score:
        avgs.append(sum(math_eng_score)/2)
        
    rank = {}
    for i, avg in enumerate(sorted(avgs, reverse=True)):
        if avg not in rank:
            rank[avg] = i+1
            
    return [rank[avg] for avg in avgs]