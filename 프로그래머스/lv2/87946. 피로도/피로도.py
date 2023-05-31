from itertools import permutations

def solution(k, dungeons):
    answer = -1
    enter_orders = permutations(range(len(dungeons)), len(dungeons))
    
    for order in enter_orders:
        temp = k
        count = 0
        for i in order:
            if temp < dungeons[i][0]:
                continue
            temp -= dungeons[i][1]
            count += 1
        if answer < count:
            answer = count
    
    return answer