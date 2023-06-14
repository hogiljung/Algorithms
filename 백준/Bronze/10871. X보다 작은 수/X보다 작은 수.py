import sys
input = sys.stdin.readline
N, X = map(int, input().split())
arr = map(int, input().split())

print(' '.join(str(n) for n in arr if n < X))