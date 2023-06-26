n = int(input())

pibo_arr = [0] + [1] * (n)

def pibo(x):
    if x <= 2:
        return pibo_arr[x]
    
    if pibo_arr[x] == 1:
        pibo_arr[x] = pibo(x-1) + pibo(x-2)
    return pibo_arr[x]

print(pibo(n))