def solution(n, t, m, p):
    answer = ''
    numbers = '0'
    n_tb = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    i = 1
    while len(numbers) // m < t:
        count = i
        temp = ''
        while i > 0:
            temp += str(i % n) if (i % n) < 10 else n_tb[str(i % n)]
            i //= n
        numbers += temp[::-1]
        i = count + 1
    
    for i in range(p-1, t*m, m):
        answer += numbers[i]
    return answer