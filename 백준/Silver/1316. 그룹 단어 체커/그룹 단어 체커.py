import sys

input = sys.stdin.readline

N = int(input())
cnt = N

for _ in range(N):
    char_check_tb = set()
    WORD = input()
    for curr in WORD:
        if curr not in char_check_tb:
            prev = curr
            char_check_tb.add(curr)
        elif prev != curr:
            cnt -= 1
            break

print(cnt)
