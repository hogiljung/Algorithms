def solution(n, arr1, arr2):
    answer = []
    
    for a1_row, a2_row in zip(arr1, arr2):
        map_row = bin(a1_row|a2_row)[2:].zfill(n)
        answer.append(map_row.replace('1', '#').replace('0', ' '))
    return answer