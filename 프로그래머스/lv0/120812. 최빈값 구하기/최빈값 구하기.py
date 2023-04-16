def solution(array):
    times_dict = {}
    for num in array:
        times_dict.setdefault(num, 0)
        times_dict[num] += 1
    
    mode = -1
    mode_times = second_times = 0
    for num, times in times_dict.items():
        if mode_times < times:
            mode = num
            mode_times = times
        elif mode_times == times:
            second_times = times
    return -1 if second_times == mode_times else mode
            
        