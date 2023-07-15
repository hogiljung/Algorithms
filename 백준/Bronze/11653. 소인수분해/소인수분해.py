N = int(input())
end = int(N**(1/2))
for i in range(2,end+1):
    while N%i == 0:
        print(i)
        N//=i
if N!=1:
    print(N)