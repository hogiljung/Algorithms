n = int(input())
array = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())

max_value = -1e10
min_value = 1e10

def dfs(i, now):
    global add, sub, mul, div, max_value, min_value

    if i == n: # index가 n이 되면 완료한 것이므로 최대 최소 계산
        max_value = max(max_value, now)
        min_value = min(min_value, now)

    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + array[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - array[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * array[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / array[i])) 
            div += 1

dfs(1, array[0])

print(max_value)
print(min_value)