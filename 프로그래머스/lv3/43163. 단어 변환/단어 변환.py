def solution(begin, target, words):
    dist = {begin:0}
    q = deque([begin])
    
    while q:
        current = q.popleft()
        
        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current]+1
                q.append(next_word)
    
    return dist.get(target, 0)

from collections import deque

def get_adjacent(current, words):
    for word in words:
        if current == word:
            continue
        for i in range(len(current)):
            if current[:i]+current[i+1:] == word[:i]+word[i+1:]:
                yield word