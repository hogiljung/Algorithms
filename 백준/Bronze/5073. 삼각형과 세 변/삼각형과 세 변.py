while (sides:=list(map(int, input().split()))) and ((total:=sum(sides)) != 0):
    maximum = max(sides)
    if maximum >= total-maximum:
        print("Invalid")
        continue

    if (count:=sides.count(maximum)) == 3:
        print("Equilateral")
    elif count == 2:
        print("Isosceles")
    else:
        sides.remove(maximum)
        if sides[0] == sides[1]:
            print("Isosceles") 
        else:
            print("Scalene")