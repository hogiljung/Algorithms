sides = list(map(int, input().split()))

if (maximum:=max(sides)) >= (other_sum:=(sum(sides)-maximum)):
    print(other_sum + other_sum-1)
else:
    print(sum(sides))