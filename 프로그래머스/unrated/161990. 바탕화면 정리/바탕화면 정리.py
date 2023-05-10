def solution(wallpaper):
    x = []
    y = []
    for i, row in enumerate(wallpaper):
        for j, icon in enumerate(row):
            if icon == '#':
                x.append(j)
                y.append(i)
            
    return [min(y), min(x), max(y)+1, max(x)+1]