def solution(people, limit):
    answer = 0
    people = sorted(people)
    big = len(people)-1
    small = 0
    
    while big > small:
        if limit >= people[big] + people[small]:
            small += 1
        big -= 1
        answer += 1
        
    if big == small:
        answer += 1
    return answer