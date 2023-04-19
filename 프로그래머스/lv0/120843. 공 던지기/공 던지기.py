def solution(numbers, k):
    answer = 2 * (k-1) % len(numbers)
    return numbers[answer]