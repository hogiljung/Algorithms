import sys
input = sys.stdin.readline

answer = 0
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = [3, 4, 5, 6, 7, 8, 9, 10, 10]

for c in input().rstrip():
    for s in alpha:
        if c in s:
            answer += time[alpha.index(s)]
print(answer)