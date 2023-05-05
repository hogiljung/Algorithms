def solution(nums):
    answer = 0
    ponketmon_tb = dict()
    for num in nums:
        ponketmon_tb.setdefault(num, 0)
        ponketmon_tb[num] += 1
    
    return len(ponketmon_tb.keys()) if len(ponketmon_tb.keys()) < len(nums)//2 else len(nums)//2
