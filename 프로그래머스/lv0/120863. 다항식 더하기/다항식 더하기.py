def solution(polynomial):
    answer = ''
    coe = 0
    const = 0
    for term in polynomial.split(" + "):
        if term[-1:] == 'x':
            coe += int(term[:-1]) if term != 'x' else 1
        else:
            const += int(term)
    
    if coe == 0:
        answer = str(0) if const == 0 else str(const)
    else:
        answer = str(coe) + 'x' if coe != 1 else 'x'
        answer += ' + ' + str(const) if const != 0 else ''
        
    return answer