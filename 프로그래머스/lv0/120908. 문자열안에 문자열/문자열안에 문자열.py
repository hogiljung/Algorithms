def solution(str1, str2):
    idx = 0
    while idx != -1:
        idx = str1.find(str2[0])
        if str1[idx:idx+len(str2)] == str2:
            print(str1[idx:len(str2)])
            return 1
        str1 = str1[idx+1:]
    return 2