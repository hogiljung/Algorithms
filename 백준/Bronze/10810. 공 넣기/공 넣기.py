import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bucket = [0]*N
for _ in range(M):
    i,j,k = map(int, input().split())

    for n in range(i-1, j):
        bucket[n] = k

print(' '.join(str(ball) for ball in bucket))