def solution(fees, records):
    answer = []
    remained_time = {}
    
    for r in records:
        rr = r.split(' ')
        remained_time.setdefault(rr[1], [])
        remained_time[rr[1]].append(rr[0])
    
    for n in remained_time.keys():
        time = 0
        times = remained_time[n]
        fee = fees[1]
        
        if len(times) % 2 != 0:
            hh, mm = map(int, times[-1].split(':'))
            time += 24*60-1 - (hh*60+mm)
            times = times[:-1]
            
        for i in range(0, len(times), 2):
            in_hh, in_mm = map(int, times[i].split(':'))
            out_hh, out_mm = map(int, times[i+1].split(':'))
            remain_minutes = (out_hh*60+out_mm) - (in_hh*60+in_mm)
            time += remain_minutes
        
        time -= fees[0]
        if time > 0:
            fee += -(-time // fees[2]) * fees[3]
        
        remained_time[n] = fee
    
    return [remained_time[n] for n in sorted(remained_time.keys())]