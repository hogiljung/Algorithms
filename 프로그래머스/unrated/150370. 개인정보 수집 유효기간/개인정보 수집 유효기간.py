def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    day_month = 28
    
    for term in terms:
        category, month = term.split()
        terms_dict[category] = int(month)
    
    t_year, t_month, t_day = map(int, today.split('.'))
    
    for i, p in enumerate(privacies):
        date, category = p.split()
        year, month, day = map(int, date.split('.'))
        month += terms_dict[category]
        day -= 1
        if day == 0:
            day = day_month
            month -= 1
        while month > 12:
            year += 1
            month -= 12
            
        delete = False
        if t_year > year:
            delete = True
        elif (year==t_year) and (t_month>month):
            delete = True
        elif (year==t_year) and (t_month==month) and (t_day>day):
            delete = True        
            
        if delete:
            answer.append(i+1)
    return answer