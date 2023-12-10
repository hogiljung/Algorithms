record_table = {1: 1, 2: 2}
n = int(input())

for i in range(3, n+1):
    record_table[i] = record_table[i-1] + record_table[i-2]

print(record_table[n] % 10007)