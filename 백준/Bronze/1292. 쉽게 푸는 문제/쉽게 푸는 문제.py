a, b = map(int, input().split())

num_arr = []
i = 1
while len(num_arr) < b:
    num_arr += [i]*i
    i += 1
print(sum(num_arr[a-1:b]))