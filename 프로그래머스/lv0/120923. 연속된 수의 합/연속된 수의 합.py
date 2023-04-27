def solution(num, total):
    answer = []
    center = int(total // num)
    if total % num == 0:
        answer = [i for i in range(center-(num)//2, center+(num)//2+1)]
    else:
        answer = [i for i in range(center-(num)//2+1, center+(num)//2+1)]
    return answer