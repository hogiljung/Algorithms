def solution(a, b):
    answer = ''
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    duration_days = sum(month_days[:a]) + b - 1
    
    return days[duration_days % 7]