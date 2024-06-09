def solution(phone_book):
    answer = True
    
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if phone_number[:i] in hash_map:
                return False
    
    return answer