import sys
input = sys.stdin.readline

for i in range(int(input().rstrip())):
    print(f"Case #{i+1}: {sum(map(int, input().rstrip().split()))}")