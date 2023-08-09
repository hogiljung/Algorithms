x_list = set()
y_list = set()

for _ in range(int(input())):
    x, y = map(int, input().split())

    x_list.add(x)
    y_list.add(y)

left, down = (min(x_list), min(y_list))
right, up = (max(x_list), max(y_list))

print((right-left) * (up-down))