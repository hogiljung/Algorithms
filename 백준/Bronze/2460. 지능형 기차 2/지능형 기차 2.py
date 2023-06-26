max = 0
curr = 0
for i in range(10):
    down, up = map(int, input().split())
    curr += (-down + up)
    if curr > max:
        max = curr
print(max)