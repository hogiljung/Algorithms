import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x):
    global id
    id += 1
    d[x] = id
    s.append(x)
    parent = d[x]

    for v in graph[x]:
        if not d[v]: 
            parent = min(parent, dfs(v))
        elif not finished[v]: 
            parent = min(parent, d[v])

    if parent == d[x]:
        scc = []
        while True:
            v = s.pop()
            scc.append(v)
            finished[v] = True

            if v == x:
                break
        scc_list.append(scc)

    return parent

if __name__ == '__main__':
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)

    id = 0
    scc_list = []
    d = [0] * (V+1)
    finished = [0] * (V+1)
    s = []

    for i in range(1, V+1):
        if not d[i]:
            dfs(i)
    
    print(len(scc_list))

    for scc in sorted(scc_list, key=lambda x: min(x)):
        print(*sorted(scc), -1)