import sys

input = sys.stdin.readline

for _ in range(int(input())):
    tc = list(map(int, input().split()))
    arr = []
    move = 0
    for n in tc[1:]:
        for i in range(len(arr)):
            if arr[i] > n:
                move += len(arr) - i
                arr.insert(i, n)
                break
        else:
            arr.append(n)

    print(f"{tc[0]} {move}")
