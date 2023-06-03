def solution(l, r):
    answer = []
    
    for i in range(int('1000000', 2)):
        n = 5 * int(bin(i)[2:])
        if n >= l and n <= r:
            answer.append(n)
    return answer or [-1]