def solution(files):
    temp = []
    
    for file in files:
        number_start_idx = 0
        number_end_idx = len(file)
        
        for c in file:
            if c.isdigit():
                number_start_idx = file.index(c)
                break
        for c in file[number_start_idx:]:
            if not c.isdigit():
                number_end_idx = number_start_idx + file[number_start_idx:].index(c)
                break

        temp.append((file, file[:number_start_idx].lower(), int(file[number_start_idx:number_end_idx])))
    
    temp.sort(key=lambda x: (x[1], x[2]))
    return [t[0] for t in temp]