tb = {}

N = input()

for c in N:
    if c in tb:
        tb[c] += 1
    else:
        tb[c] = 1

tb["6"] = (tb.get("6", 0) + tb.get("9", 0) + 1) // 2
tb["9"] = 0

print(max([v for v in tb.values()]))
