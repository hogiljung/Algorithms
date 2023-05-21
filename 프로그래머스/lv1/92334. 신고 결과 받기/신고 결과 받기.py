def solution(id_list, report, k):
    answer = []
    report_dict = {}
    reporter_dict = {}
    stopped = set()
    
    for r in set(report):
        reporter, reported = r.split()
        reporter_dict.setdefault(reporter, set())
        reporter_dict[reporter].add(reported)
        
        report_dict.setdefault(reported, 0)
        report_dict[reported] += 1
        
    for reported in report_dict:
        if report_dict[reported] >= k:
            stopped.add(reported)
            
    for id in id_list:
        if id in reporter_dict:
            answer.append(len(reporter_dict[id]&stopped))
        else:
            answer.append(0)
    
    return answer