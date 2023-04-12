def solution(n, times):
    answer = 0
    maximum = min(times) * n # 가장 수행 시간이 빠른 사람 * 사람 수를 최대 시간으로 놓는다.
    minimum = min(times)
    
    while not (minimum+1 == maximum):
        medium = (maximum + minimum) // 2 # 이진 탐색을 위한 값

        if sum([medium // time for time in times]) >= n: # 주어진 시간을 심사원들의 수행 시간으로 나눈 합이 심사 인원보다 많거나 같으면 시간을 줄인다.
            maximum = medium
        else:
            minimum = medium
            
    return maximum