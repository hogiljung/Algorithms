def solution(s):
    answer = ''
    for word in s.split(' '):
        if word == '':
            answer += ' '
        else:
            answer += word[0].upper() + word[1:].lower() + ' '
    return answer[:-1]