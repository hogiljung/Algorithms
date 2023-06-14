s = input().upper()
counts = sorted(((s.count(c), c) for c in set(s)), reverse=True)
if len(counts) == 1:
    print(counts[0][1])
else:
    print(counts[0][1] if counts[0][0] != counts[1][0] else '?')