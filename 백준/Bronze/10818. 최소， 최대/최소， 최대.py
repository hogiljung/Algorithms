import sys
input = sys.stdin.readline
input()
arr = list(map(int, input().split()))
print(min(arr), max(arr))