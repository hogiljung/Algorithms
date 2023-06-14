import sys
input = sys.stdin.readline
maximum = 0
max_idx = 0
for i in range(9):
    n = int(input())
    if maximum < n:
        maximum = n
        max_idx = i+1
print(f"{maximum}\n{max_idx}")