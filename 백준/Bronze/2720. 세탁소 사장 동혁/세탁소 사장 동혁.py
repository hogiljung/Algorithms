change = [25, 10, 5, 1]

for _ in range(int(input())):
    n = int(input())

    for i in range(len(change)):
        count, n = divmod(n, change[i])
        print(count, end=' ')
    print()