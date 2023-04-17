def solution(num_list):
    even_count = sum(1 for n in num_list if n%2 == 0)
    odd_count = len(num_list) - even_count
    return [even_count, odd_count]