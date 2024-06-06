def solution(date1, date2):
    def date_to_str(date):
        return map(str, date)
    
    date1_year, date1_month, date1_day = date_to_str(date1)
    date2_year, date2_month, date2_day = date_to_str(date2)
    
    if len(date1_year) < len(date2_year):
        return 1
    elif len(date1_year) > len(date2_year):
        return 0
    else:
        if date1_year[0] < date2_year[0]:
            return 1
        elif date1_year[0] > date2_year[0]:
            return 0
        if len(date1_year) > 1:
            if date1_year[1] < date2_year[1]:
                return 1
            elif date1_year[1] > date2_year[1]:
                return 0
        if len(date1_year) > 2:
            if date1_year[2] < date2_year[2]:
                return 1
            elif date1_year[2] > date2_year[2]:
                return 0
        if len(date1_year) > 3:
            if date1_year[3] < date2_year[3]:
                return 1
            elif date1_year[3] > date2_year[3]:
                return 0
    
    if len(date1_month) < len(date2_month):
        return 1
    elif len(date1_month) > len(date2_month):
        return 0
    else:
        if date1_month[0] < date2_month[0]:
            return 1
        elif date1_month[0] > date2_month[0]:
            return 0
        if len(date1_month) > 1:
            if date1_month[1] < date2_month[1]:
                return 1
            elif date1_month[1] > date2_month[1]:
                return 0
    
    if len(date1_day) < len(date2_day):
        return 1
    elif len(date1_day) > len(date2_day):
        return 0
    else:
        if date1_day[0] < date2_day[0]:
            return 1
        elif date1_day[0] > date2_day[0]:
            return 0
        if len(date1_day) > 1:
            if date1_day[1] < date2_day[1]:
                return 1
            elif date1_day[1] > date2_day[1]:
                return 0

    return 0