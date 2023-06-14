N = int(input())
answer = N
for _ in range(N):
    s = input()
    while s:
        n = s.count(s[0])
        if s[0]*n != s[:n]:
            answer -= 1
            break
        s = s[n:]
print(answer)