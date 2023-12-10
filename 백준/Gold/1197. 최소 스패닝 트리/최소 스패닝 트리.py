import sys
input= sys.stdin.readline

def get_parent(parent_table, v):
    if parent_table[v] == v: return v
    parent_table[v] = get_parent(parent_table, parent_table[v])
    return parent_table[v]

def union_parent(parent_table, a, b):
    a = get_parent(parent_table, a)
    b = get_parent(parent_table, b)
    if a < b: parent_table[b] = a
    else: parent_table[a] = b

def find_parent(parent_table, a, b):
    a = get_parent(parent_table, a)
    b = get_parent(parent_table, b)
    if a == b: return 1
    else: return 0

class Edge:
    def __init__(self, v1, v2, cost):
        self.v = [v1, v2]
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def solution():
    V, E = map(int, input().split())

    edges = []
    for _ in range(E):
        v1, v2, cost = map(int, input().split())
        edges.append(Edge(v1, v2, cost))
    edges.sort()

    parent_table = [i for i in range(V+1)]

    total_cost = 0
    for edge in edges:
        if not find_parent(parent_table, edge.v[0], edge.v[1]):
            total_cost += edge.cost
            union_parent(parent_table, edge.v[0], edge.v[1])
    
    print(total_cost)

if __name__ == "__main__":
    solution()