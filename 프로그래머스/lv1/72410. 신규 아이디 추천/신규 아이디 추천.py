import re

def solution(new_id):
    answer = ''
    temp = re.sub('[^a-z\d\_\-\.]','',new_id.lower())
    temp = re.sub('\.\.+', '.', temp)
    temp = re.sub('^\.', '', temp)

    if temp == '':
        temp = 'a'
    
    temp = re.sub('\.$','', temp[:15])
    
    if len(temp) < 3:
        return temp.ljust(3, temp[-1])
    
    answer = temp
    return answer