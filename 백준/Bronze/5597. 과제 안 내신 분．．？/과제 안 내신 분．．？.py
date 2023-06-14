import sys
input = sys.stdin.readline

submit_nums = [i for i in range(1, 31)]

for _ in range(28):
    submit_nums[int(input())-1] = 0

for submit in submit_nums:
    if submit != 0:
        print(submit)