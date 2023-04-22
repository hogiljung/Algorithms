def solution(sizes):
    min_width = 0
    min_height = 0
    
    for size in sizes:
        width1, width2 = max(min_width, size[0]), max(min_width, size[1])
        height1, height2 = max(min_height, size[1]), max(min_height, size[0])
        
        min_width, min_height = (width1, height1) if width1*height1 < width2*height2 else (width2, height2)
    
    return min_width * min_height