def solution(n, arr1, arr2):
    answer = []
    
    for a1_row, a2_row in zip(arr1, arr2):
        a1_row_bin, a2_row_bin = bin(a1_row)[2:].zfill(n), bin(a2_row)[2:].zfill(n)
        map_row = ''
        
        for a1, a2 in zip(a1_row_bin, a2_row_bin):
            if a1 == '0' and a2 == '0':
                map_row += ' '
            else:
                map_row += '#'
                
        answer.append(map_row)
    return answer