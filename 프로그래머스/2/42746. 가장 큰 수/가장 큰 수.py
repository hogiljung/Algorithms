from functools import cmp_to_key

def solution(numbers):
    # numbers의 모든 요소를 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    # 커스텀 비교 함수 정의
    def compare(x, y):
        return (y + x > x + y) - (y + x < x + y)
    
    # 문자열 리스트를 커스텀 비교 함수 기준으로 정렬
    sorted_numbers = sorted(str_numbers, key=cmp_to_key(compare))
    
    # 정렬된 문자열 리스트를 합침
    largest_number = ''.join(sorted_numbers)
    
    # 결과가 '0000' 같은 경우를 대비하여 int로 변환 후 다시 문자열로 변환
    if largest_number[0] == "0":
        return "0"
    else:
        return largest_number