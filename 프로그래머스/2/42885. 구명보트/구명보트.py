def solution(people, limit):
    answer = 0
    n = len(people)
    check = [False] * n
    
    people.sort()
    
    l = 0
    r = n-1
    
    while l <= r:
        current = people[r]
        r -= 1
        
        if current + people[l] <= limit:
            l += 1
            
        answer += 1
    
    return answer