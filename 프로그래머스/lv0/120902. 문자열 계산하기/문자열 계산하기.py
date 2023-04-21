def solution(my_string):
    s = my_string.split()
    answer = int(s[0])
    for i in range(1, len(s), 2):
        answer += int(s[i+1]) if s[i] == '+' else -int(s[i+1])
    return answer