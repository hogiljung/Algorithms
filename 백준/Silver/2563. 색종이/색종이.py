paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(int(input())):
    left, top = map(int, input().split())

    for i in range(10):
        for j in range(10):
            paper[top+i][left+j] = 1
    
count = 0
for i in range(100):
    count += paper[i].count(1)

print(count)