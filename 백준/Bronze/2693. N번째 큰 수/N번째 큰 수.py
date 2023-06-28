N = int(input())

for _ in range(N):
    arr = []
    for n in map(int, input().split()):
        arr.append(n)
    print(sorted(arr)[-3])