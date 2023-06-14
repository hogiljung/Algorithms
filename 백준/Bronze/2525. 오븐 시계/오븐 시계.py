h, m = map(int, input().split())
need_m = int(input())

total = h*60 + m + need_m
h = total // 60 % 24
m = total % 60
print(f"{h} {m}")