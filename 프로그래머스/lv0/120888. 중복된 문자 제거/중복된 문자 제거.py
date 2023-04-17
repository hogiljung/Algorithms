def solution(my_string):
    answer = ''
    dict = {}
    for c in my_string:
        dict[c] = True
    
    for key in my_string:
        if key in dict:
            answer += key
            del dict[key]
    return answer