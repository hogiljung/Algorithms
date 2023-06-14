import sys
input = sys.stdin.readline

alpha = [-1]*26
for i, c in enumerate(input().rstrip()):
    idx = ord(c)-ord('a')
    if alpha[idx] == -1:
        alpha[idx] = i
print(*alpha)