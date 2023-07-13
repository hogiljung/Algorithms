place = [1, 1]
maximum = 0

for i in range(1, 10):
    num_arr = list(map(int, input().split()))
    if max(num_arr) > maximum:
        maximum = max(num_arr)
        place = [i, num_arr.index(maximum) + 1]

print(maximum)
print(place[0], place[1])