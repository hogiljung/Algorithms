def solution(n, times):
    at_most = min(times) * n
    
    answer = at_most
    
    # 심사 시간이 가장 짧은 시간이 모두를 검사하는 시간을 최댓값으로 본다.
    l, r = 1, at_most

    while l <= r:
        mid = (l + r) // 2
        
        total_checked = sum([mid//time for time in times])

        if total_checked < n:
            l = mid + 1
        else:
            answer = min(answer, mid)
            r = mid - 1
            
    return answer