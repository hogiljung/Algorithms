while (n:=int(input())) != -1:
    factor_arr = [1]
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            factor_arr += [i, n//i]
    
    if n == sum(factor_arr):
        print(f"{n} = " + ' + '.join(map(str, sorted(factor_arr))))
    else:
        print(f"{n} is NOT perfect.")