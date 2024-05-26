def solution(numbers):
    # numbers의 모든 요소를 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    str_numbers.sort(key=lambda x: (x*3)[:4], reverse=True)
    
    largest_number = "".join(str_numbers)
    
    # 결과가 '0000' 같은 경우를 대비
    if largest_number[0] == "0":
        return "0"
    else:
        return largest_number