A = int(input())
B = input()
answer = 0
for i, b in enumerate(B[::-1]):
    temp = A*int(b)
    print(temp)
    answer += temp * (10**i)
print(answer)