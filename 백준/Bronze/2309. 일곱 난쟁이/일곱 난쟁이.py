heights = []
check = False

for i in range(9):
    heights.append(int(input()))

for i in range(len(heights)):
    for j in range(i+1, len(heights)):
        if sum(heights[:i] + heights[i+1:j] + heights[j+1:]) == 100:
            heights = sorted(heights[:i] + heights[i+1:j] + heights[j+1:])
            check = True
            break
    if check:
        break

for height in heights:
    print(height)