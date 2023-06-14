import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
maximum = max(scores)
new_scores = list(map(lambda x: x/maximum*100, scores))
print((sum(new_scores))/N)