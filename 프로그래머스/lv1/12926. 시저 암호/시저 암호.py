def solution(s, n):
    answer = ''
    
    for c in s:
        if c != ' ':
            if c >= 'a' and c <= 'z':
                answer += chr((ord(c)+n-ord('a')) % 26 + ord('a'))
            else:
                answer += chr((ord(c)+n-ord('A')) % 26 + ord('A'))
        else:
            answer += c
    
    return answer

    
    