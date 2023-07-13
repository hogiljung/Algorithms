n, b = map(int, input().split())

ntob = ''

while n:
    n, d = divmod(n, b)
    if d >= 10:
        ntob += chr(d+55)
    else:
        ntob += str(d)

print(ntob[::-1])