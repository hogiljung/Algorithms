def solution(quiz):
    answer = []
    for q in quiz:
        exp, result = q.split(' = ')
        exp_items = exp.replace('- ', '+ -').replace('--', '').split(' + ')
        answer.append('O' if sum(map(int, exp_items)) == int(result) else 'X')
    return answer