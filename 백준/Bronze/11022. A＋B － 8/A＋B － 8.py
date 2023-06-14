import sys
input = sys.stdin.readline

for i in range(int(input().rstrip())):
    a, b = map(int, input().rstrip().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")