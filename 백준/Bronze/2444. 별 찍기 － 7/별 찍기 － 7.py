N = int(input())

for i in range(-N+1, N):
    for j in range(abs(i)):
        print(' ', end='')
    for j in range(2*(N-abs(i))-1):
        print('*', end='')
    print()