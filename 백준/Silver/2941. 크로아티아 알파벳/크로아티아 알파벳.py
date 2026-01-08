word = input()

cnt = 0
i = 0
while i < len(word):
    if word[i : i + 2] in ("c=", "c-", "d-", "lj", "nj", "s=", "z="):
        cnt += 1
        i += 2
    elif word[i : i + 3] == "dz=":
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1

print(cnt)
