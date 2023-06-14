import sys
input = sys.stdin.readline

N, M = map(int, input().split())
buckets = list(range(1,N+1))

for _ in range(M):
    i,j = map(int, input().split())
    temp = buckets[i-1:j]
    for idx in range(i-1, j):
        buckets[idx] = temp.pop()

print(' '.join(str(n) for n in buckets))