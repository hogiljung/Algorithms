angles = []
for _ in range(3):
    angles.append(int(input()))

if sum(angles) != 180:
    print("Error")
else:
    angle = angles.pop()
    
    if angles.count(angle) == 2:
        print("Equilateral")
    elif angles.count(angle) == 1:
        print("Isosceles")
    else:
        print("Isosceles") if angles[0] == angles[1] else print("Scalene")