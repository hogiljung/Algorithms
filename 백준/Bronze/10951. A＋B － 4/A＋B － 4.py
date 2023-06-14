import sys
input = sys.stdin.readline
while (v_sum := sum(map(int, input().rstrip().split()))):
    print(v_sum)