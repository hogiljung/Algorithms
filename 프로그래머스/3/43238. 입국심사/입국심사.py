def solution(n, times):
    at_most = min(times) * n
    
    answer = 0
    
    # 심사 시간이 가장 짧은 시간이 모두를 검사하는 시간을 최댓값으로 본다.
    l, r = 1, at_most

    # 이분 탐색으로 최소 시간을 찾는다.
    while l < r:
        mid = (l + r) // 2
        
        # 각각 걸리는 시간으로 전체 시간을 나눈 몫을 더하면 검사한 인원 수가 나온다.
        total_checked = sum([mid//time for time in times])

        if total_checked < n:
            l = mid + 1
        else:
            r = mid
            
    answer = l
            
    return answer