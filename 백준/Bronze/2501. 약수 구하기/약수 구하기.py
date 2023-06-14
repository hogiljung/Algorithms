N, n = map(int, input().split())
measures = []
for i in range(1, N+1):
    if N % i == 0:
        measures.append(i)

print(measures[n-1] if n <= len(measures) else 0)