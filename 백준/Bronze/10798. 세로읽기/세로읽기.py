str_arr = []

for _ in range(5):
    str_arr.append(input())

for j in range(15):
    for i in range(5):
        if len(str_arr[i]) > j:
            print(str_arr[i][j], end='')