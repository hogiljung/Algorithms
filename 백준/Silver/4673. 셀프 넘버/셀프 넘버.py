def cal_dn(n):
    dn = n
    n_str = str(n)
    for c in n_str:
        dn += int(c)
    return dn


tb = set()

for check_n in range(1, 10000):
    n = check_n
    while True:
        dn = cal_dn(n)

        if dn in tb or dn > 10000:
            break

        tb.add(dn)
        n = dn

selfnumber_cnt = 0
for check_n in range(1, 10001):
    if check_n not in tb:
        print(check_n)
