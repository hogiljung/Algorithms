import sys

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
y, x, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    if board[y][x] == 0:
        board[y][x] = 2
        cnt += 1

    moved = False
    for _ in range(4):
        d = (d + 3) % 4
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
            y = ny
            x = nx
            moved = True
            break

    if moved:
        continue

    back = (d + 2) % 4
    ny = y + dy[back]
    nx = x + dx[back]

    if not (0 <= ny < N and 0 <= nx < M) or board[ny][nx] == 1:
        break

    y = ny
    x = nx

print(cnt)
