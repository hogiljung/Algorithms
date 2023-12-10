import sys
sys.setrecursionlimit(2000)

INF = 10e9

def get_sugar(sugar_table, n):
    if n < 3: return INF
    if n == 3 or n == 5: return 1
    if sugar_table[n]: return sugar_table[n]
    min_prev = min(get_sugar(sugar_table, n-5), get_sugar(sugar_table, n-3))
    if min_prev == INF:
        sugar_table[n] = INF
    else:
        sugar_table[n] = min_prev + 1
    return sugar_table[n]

def solution():
    sugar_table = [0] * 5001

    N = int(input())

    if (answer := get_sugar(sugar_table, N)) != INF:
        print(answer)
    else:
        print(-1)

if __name__ == "__main__":
    solution()