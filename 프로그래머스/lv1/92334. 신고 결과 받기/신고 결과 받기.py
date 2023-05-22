def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report_dict = {x: 0 for x in id_list}
    
    for r in set(report):
        report_dict[r.split()[1]] += 1
        
    for r in set(report):
        if report_dict[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer