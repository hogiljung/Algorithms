def solution(arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        cell = []
        for x, y in zip(a, b):
            cell.append(x+y)
        answer.append(cell)
        
    return answer