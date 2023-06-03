def solution(land):
    answer = 0
    temp_land = [[0 for i in range(len(land[0]))] for i in range(len(land))]
    
    for i in range(-1, len(land)-1):
        for j in range(len(land[0])):
            temp = land[i+1][j] + max(temp_land[i][:j] + temp_land[i][j+1:])
            if temp > temp_land[i+1][j]: temp_land[i+1][j] = temp
            
    answer = max(temp_land[-1])        
    return answer