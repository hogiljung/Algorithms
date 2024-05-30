def solution(numbers, target):
    answer = 0
    
    def dfs(arr, i):
        nonlocal answer
        
        if i == len(numbers):
            if sum(arr) == target:
                answer += 1
            return
        
        dfs(arr + [numbers[i]], i+1)
        dfs(arr + [-numbers[i]], i+1)
    
    dfs([], 0)
    
    return answer