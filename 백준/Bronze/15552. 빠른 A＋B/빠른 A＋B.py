import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    print(sum(map(int, input().rstrip().split())))