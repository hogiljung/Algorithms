a,b,c = map(int, input().split())

if a==b or a==c:
    if b==c:
        print(10000+a*1000)
    else:
        print(1000+a*100)
else:
    if b==c:
        print(1000+b*100)
    else:
        print(max(a,b,c)*100)