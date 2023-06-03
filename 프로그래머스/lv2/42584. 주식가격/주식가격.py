def solution(prices):
    answer = [0] * len(prices)
    s = []
    
    for i in range(len(prices)):
        price = prices[i]
        while s and s[-1][0] > price:
            _, idx = s.pop()
            answer[idx] = i - idx
        s.append((price, i))
    
    for i in range(len(s)):
        answer[s[i][1]] = len(prices)-1-s[i][1]
    return answer