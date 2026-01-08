import sys
input = sys.stdin.readline

AREA_X = 100
AREA_Y = 100
area = [[0 for _ in range(AREA_X)] for _ in range(AREA_Y)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, min(x + 10, AREA_X)):
        for j in range(y, min(y + 10, AREA_Y)):
            area[j][i] = 1

print(sum([sum(area[i]) for i in range(len(area))]))