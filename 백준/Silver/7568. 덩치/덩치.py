import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    h, w = map(int, input().split())
    arr.append((h, w))

for curr_h, curr_w in arr:
    rank = 1
    for h, w in arr:
        if h > curr_h and w > curr_w:
            rank += 1
    print(rank)
