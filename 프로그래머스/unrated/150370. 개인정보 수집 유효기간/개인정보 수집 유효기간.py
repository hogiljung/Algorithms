def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    
    for term in terms:
        category, month = term.split()
        terms_dict[category] = int(month)*28
    
    today_year, today_month, today_day = map(int, today.split('.'))
    today = today_year*12*28 + today_month*28 + today_day
    
    for i, p in enumerate(privacies):
        date, category = p.split()
        year, month, day = map(int, date.split('.'))
        entered_day = year*12*28 + month*28 + day
        expired_day = entered_day + terms_dict[category] - 1
        if today > expired_day:
            answer.append(i+1)
        
    return answer