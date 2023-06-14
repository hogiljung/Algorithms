import sys
input = sys.stdin.readline
N = int(input().rstrip())
for i in range(N):
    print(' '*(N-(i+1))+'*'*(i+1))