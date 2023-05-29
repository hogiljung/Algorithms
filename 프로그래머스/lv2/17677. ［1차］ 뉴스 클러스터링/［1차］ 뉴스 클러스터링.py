from collections import Counter

def solution(str1, str2):
    answer = 1
    str1_count = Counter([str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()])
    str2_count = Counter([str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()])
    
    if bool(str1_count|str2_count):
        answer = sum((str1_count&str2_count).values()) / sum((str1_count|str2_count).values())
        
    return int(answer * 65536)