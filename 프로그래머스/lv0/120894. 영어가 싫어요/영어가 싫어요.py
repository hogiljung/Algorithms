def solution(numbers):
    numbers_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, s in enumerate(numbers_str):
        numbers = numbers.replace(s, str(i))
    return int(numbers)