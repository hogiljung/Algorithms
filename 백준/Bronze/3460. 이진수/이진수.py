count = int(input())
for _ in range(count):
    n = int(input())
    for i, c in enumerate(str(bin(n))[2:][::-1]):
        if c == '1':
            print(i, end=' ')