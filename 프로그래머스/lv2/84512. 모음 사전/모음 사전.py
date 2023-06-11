def solution(word):
    answer = 0
    spell = 'A E I O U'.split()
    word_dict = {}
    temp = ''
    
    def add_word(word_dict, temp, length):
        if length <= 0:
            return
        
        for i in range(len(spell)):
            temp += spell[i]
            word_dict[temp] = len(word_dict)+1
            add_word(word_dict, temp, length-1)
            temp = temp[:-1]
    
    add_word(word_dict, temp, 5)
    
    return word_dict[word]