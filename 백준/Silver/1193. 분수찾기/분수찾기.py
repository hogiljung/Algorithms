N = int(input())

floor = 1
count = 1

while count < N:
    floor += 1
    count += floor

move = count-N
a = 1 + move
b = floor - move

if floor % 2 != 0:
    print(f"{a}/{b}")
else:
    print(f"{b}/{a}")