def solution(n, words):
    answer = [0, 0]
    history = []
    for i, word in enumerate(words):
        if word in history or (history and word[0] != history[-1][-1]):
            print(word, history)
            answer = [i%n+1, i//n+1]
            return answer
        else:
            history.append(word)
            
    return answer