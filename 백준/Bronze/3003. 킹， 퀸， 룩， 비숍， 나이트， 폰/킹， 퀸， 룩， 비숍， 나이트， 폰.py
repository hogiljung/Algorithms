needs = [1, 1, 2, 2, 2, 8]
answer = []
for n, need in zip(map(int, input().split()), needs):
    answer.append(need - n)
print(*answer)