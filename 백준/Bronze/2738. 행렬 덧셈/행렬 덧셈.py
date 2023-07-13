n, m = map(int, input().split())

matrix = [[] for _ in range(2)]

for i in range(2):
    for _ in range(n):
        matrix[i].append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(matrix[0][i][j] + matrix[1][i][j], end=' ')
    print()