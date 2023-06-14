import sys

total_price = int(input())
input()
for i in sys.stdin:
    price, count = map(int, i.split())
    total_price -= price * count

print('Yes' if total_price == 0 else 'No')