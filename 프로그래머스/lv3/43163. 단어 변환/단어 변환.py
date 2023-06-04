from collections import deque
def solution(begin, target, words):
    INF = int(1e9)
    answer = INF
    words = [begin] + words
    graph = [[0 for _ in range(len(words))] for _ in range(len(words))]
    s = []
    for i, word in enumerate(words):
        for j, other_word in enumerate(words):
            diff = 0
            for c1, c2 in zip(word, other_word):
                if i == j:
                    continue
                if c1 != c2:
                    diff += 1
            if diff == 1:
                graph[i][j] = 1

    def bfs(v):
        nonlocal answer
        q = deque()
        q.append((v, 0))
        visited = [False] * len(words)
        while q:
            start, count = q.popleft()
            if words[start] == target:
                if count < answer:
                    answer = count

            visited[start] = True
            for end in range(len(graph)):
                if graph[start][end] != 0 and not visited[end]:
                    q.append((end, count+1))
    bfs(0)
    return answer if answer != INF else 0

    
    